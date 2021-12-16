import pygame
import random

WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
PURPLE = (51, 0, 51)
WHITE = (255, 255, 255)
FPS = 30

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y, img='PL1.png'):

        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.change_x = 0
        self.change_y = 0
        self.walls = None

        self.crowns = None
        self.collected_crowns = 0
        self.diamonds = None
        self.collected_diamonds = 0

        self.monsters = pygame.sprite.Group()
        self.alive = True

    def update(self):
        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


        diamonds_hit_list = pygame.sprite.spritecollide(self, self.diamonds, False)
        for diamond in diamonds_hit_list:
            self.collected_diamonds += 1
            diamond.kill()

        crowns_hit_list = pygame.sprite.spritecollide(self, self.crowns, False)
        for crown in crowns_hit_list:
            self.collected_crowns += 1
            crown.kill()

        if pygame.sprite.spritecollide(self, self.monsters, False):
            self.alive = False

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, WIDTH, HEIGHT):
        super().__init__()

        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(BLACK)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x




class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y, img='Diamond.png'):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Crown(pygame.sprite.Sprite):
    def __init__(self, x , y, img = 'Crown1.png'):
        super().__init__()

        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, img = 'Monster img.png'):
        super().__init__()
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.start = x
        self.stop = x + random.randint(180, 240)
        self.direction = 1

    def update(self):
        if self.rect.x >= self.stop:
            self.rect.x = self.stop
            self.direction = -1

        if self.rect.x <= self.start:
            self.rect.x = self.start
            self.direction = 1

        self.rect.x += self.direction * 2




pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Maze')



all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()

wall_coords = [
    [0, 0, 10, 600],
    [790, 0, 10, 600],
    [10, 0, 790, 10],
    [0, 200, 100, 10],
    [0, 590, 600, 10],
    [450, 400, 10, 200],
    [550, 450, 250, 10],

]


for coord in wall_coords:
    wall = Wall(coord[0], coord[1], coord[2], coord[3])
    wall_list.add(wall)
    all_sprite_list.add(wall)


diamonds_list = pygame.sprite.Group()
diamonds_coord = [[100, 140], [235,250], [400,234]]

for coord in diamonds_coord:
    diamond = Diamond(coord[0], coord[1])
    diamonds_list.add(diamond)
    all_sprite_list.add(diamond)




crowns_list = pygame.sprite.Group()
crowns_coord = [[550, 500]]

for coord in crowns_coord:
    crown = Crown(coord[0], coord[1])
    crowns_list.add(crown)
    all_sprite_list.add(crown)

monsters_list = pygame.sprite.Group()
monster_coord = [[1, 500], [400, 50]]
for coord in monster_coord:
    monster = Monster(coord[0], coord[1])
    monsters_list.add(monster)
    all_sprite_list.add(monster)


player = Player(50, 50)
player.walls = wall_list
all_sprite_list.add(player)



player.diamonds = diamonds_list
player.monsters = monsters_list
player.crowns = crowns_list

font = pygame.font.SysFont('Arial', 24, True)
text = font.render('END', True, WHITE)
text1 = font.render('Win', True, WHITE)

clock = pygame.time.Clock()
done = False


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.change_x = 3
            elif event.key == pygame.K_a:
                player.change_x = -3
            elif event.key == pygame.K_w:
                player.change_y = -3
            elif event.key == pygame.K_s:
                player.change_y = 3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.change_x = 0
            elif event.key == pygame.K_a:
                player.change_x = 0
            elif event.key == pygame.K_w:
                player.change_y = 0
            elif event.key == pygame.K_s:
                player.change_y = 0


    screen.fill(PURPLE)



    if not player.alive:
        screen.blit(text, (100,100))
    else:
        all_sprite_list.update()
        all_sprite_list.draw(screen)

    if player.collected_crowns == 1 and player.alive:
        screen.blit(text1, (100, 100))
    else:
       all_sprite_list.draw(screen)




    pygame.display.flip()
    clock.tick(60)


pygame.quit()






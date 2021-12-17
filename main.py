import pygame
import random

'''размер игрового экрана, цвета в игре и скорость обновления изображения'''
WIDTH = 800
HEIGHT = 600
BLACK = (0, 0, 0)
PURPLE = (51, 0, 51)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
FPS = 30

class Player(pygame.sprite.Sprite):
    '''функция, отвечающая за начальные данные персонажа игрока'''
    def __init__(self, x, y, img='PL1.png'):
        super().__init__()
        '''применяем изображение нпс игрока и устанавливаем персонажа на позицию'''
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        '''устанавливаем начально, что сдвигов не было, мы не трогали стены, 
        мы не собирали алмазы, спрайты монстров задействованы и персонаж не умер'''
        self.change_x = 0
        self.change_y = 0
        self.walls = None

        self.crowns = None
        self.collected_crowns = 0
        self.diamonds = None
        self.collected_diamonds = 0

        self.monsters = pygame.sprite.Group()
        self.alive = True

    '''функция, отвечающая за движения игрока и его взаимодействие с окружающими объектами'''
    def update(self):
        '''если был сдвиг по оси x, то мы добавлаем к значению x в координатах
         положения персонажа игрока значение сдвига по оси х'''
        self.rect.x += self.change_x
        '''если игрок идет на позицию, где стена, персонаж игрока не будет двигаться'''
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        '''если выполнено движение по оси x, то в зависомости от значения сдвига, 
        персонаж игрока пойдет или вправо (x>0), или влево(x<0)'''
        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
        '''если был сдвиг по оси y, то мы добавлаем к значению y в координатах
         положения персонажа игрока значение сдвига по оси y'''
        self.rect.y += self.change_y
        '''если игрок идет на позицию, где стена, персонаж игрока не будет двигаться'''
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        '''если выполнено движение по оси y, то в зависомости от значения сдвига, 
        персонаж игрока пойдет или вверх (y>0), или вниз(y<0)'''
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

        '''если игрок дошел до алмаза, то он засчитывается в счетчик наколенных алмазов и 
        уничтожает сам алмаз'''
        diamonds_hit_list = pygame.sprite.spritecollide(self, self.diamonds, False)
        for diamond in diamonds_hit_list:
            self.collected_diamonds += 1
            diamond.kill()

        crowns_hit_list = pygame.sprite.spritecollide(self, self.crowns, False)
        for crown in crowns_hit_list:
            self.collected_crowns += 1
            crown.kill()
        '''если игрок дошел до зоны движения монстра, то он умирает'''
        if pygame.sprite.spritecollide(self, self.monsters, False):
            self.alive = False

class Wall(pygame.sprite.Sprite):
    '''функция, отвечающая за создание стен'''
    def __init__(self, x, y, WIDTH, HEIGHT):
        super().__init__()
        '''формируем стены по установленным ширине и высоте с цветом BLACK'''
        self.image = pygame.Surface([WIDTH, HEIGHT])
        self.image.fill(BLACK)
        '''устанавливаем стены на указанные позиции'''
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

class Diamond(pygame.sprite.Sprite):
    '''функция, отвечающая за создание алмазов'''
    def __init__(self, x, y, img='Diamond.png'):
        super().__init__()
        '''выгружаем изображение алмаза и устанавливаем несколько на указанные позиции'''
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
    '''функция, отвечающая за создание монстров'''
    def __init__(self, x, y, img = 'Monster img.png'):
        super().__init__()
        '''выгружаем изображение монстра и устаналиваем несколько на указанные позиции'''
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        '''устанавливаем зону действия монстра по оси x'''
        self.start = x
        self.stop = x + random.randint(180, 240)
        self.direction = 1

    '''функция, отвечающая за движение монстра'''
    def update(self):
        '''если начальное положение монстра правее его допустимой зоны действия по оси x,
        то начальное положение меняется на самую правую зону зону действия'''
        if self.rect.x >= self.stop:
            self.rect.x = self.stop
            self.direction = -1
        '''если начальное положение монстра левее его допустимой зоны действия по оси x,
        то начальное положение меняется на самую левую зону зону действия'''
        if self.rect.x <= self.start:
            self.rect.x = self.start
            self.direction = 1

        self.rect.x += self.direction * 2


'''иниализация запуска игры'''
pygame.init()
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('ЛАБИРИНТ')


'''указываем, что список спрайтов и стен в группе спрайтов '''
all_sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()
'''список стен с координтами x,y и размерами ширина, высота'''
wall_coords = [
    [0, 0, 800, 10],
    [0, 590, 800, 10],
    [0, 0, 10, 600],
    [790, 0, 10, 600],
    [10, 450, 40, 20],
    [10,60,100,20],
    [90,80,20,70],
    [60,130,30,20],
    [160,10,20,60],
    [10,200,40,20],
    [130, 200, 50, 130],
    [100,200,30,20],
    [160,190,90,20],
    [160,120,20,70],
    [180,120,50,20],
    [230,60,20,80],
    [230,60,80,20],
    [230,190,20,80],
    [60,270,20,130],
    [60,380,130,20],
    [100,400,20,140],
    [60,520,60,20],
    [170,380,20,70],
    [100,500,170,20],
    [240,410,30,110],
    [240,410,50,20],
    [170,570,100,20],
    [300,130,50,90],
    [300,200,110,20],
    [300,270,60,90],
    [240,320,120,40],
    [340,270,20,160],
    [320,480,50,60],
    [320,520,110,20],
    [700, 60, 40, 30],
    [740, 220, 50, 20],
    [770, 410, 20, 30],
    [620, 430, 100, 20],
    [670, 450, 50, 70],
    [620, 500, 120, 20],
    [680, 490, 60, 50],
    [580, 570, 50, 20],
    [470, 10, 20, 70],
    [470, 60, 50, 20],
    [360, 60, 60, 20],
    [400, 60, 20, 90],
    [400, 130, 90, 20],
    [410, 270, 80, 40],
    [410, 360, 160, 20],
    [470, 270, 20, 90],
    [550, 360, 20, 110],
    [420, 430, 80, 40],
    [480, 470, 90, 50],
    [480, 520, 50, 20],
    [460, 200, 100, 20],
    [540, 130, 20, 70],
    [540, 130, 70, 20],
    [570, 60, 40, 70],
    [570, 60, 80, 30],
    [660, 140, 80, 30],
    [660, 140, 30, 60],
    [610, 200, 80, 90],
    [540, 270, 120, 40],
    [620, 290, 120, 30],
    [620, 290, 30, 90],
    [700, 290, 20, 90],
    [720, 290, 20,70]
]

'''добавляем данные о стенах в список стен и список спрайтов'''
for coord in wall_coords:
    wall = Wall(coord[0], coord[1], coord[2], coord[3])
    wall_list.add(wall)
    all_sprite_list.add(wall)

'''указываем, что список алмазов в группе спрайтов и указываем координаты алмазов'''
diamonds_list = pygame.sprite.Group()
diamonds_coord = [[510, 430], [130,410], [50,90]]

'''добавляем данные об алмазах в список алмазов и список спрайтов'''
for coord in diamonds_coord:
    diamond = Diamond(coord[0], coord[1])
    diamonds_list.add(diamond)
    all_sprite_list.add(diamond)

'''указываем, что список монстров в группе спрайтов и указываем координаты монстров'''


crowns_list = pygame.sprite.Group()
crowns_coord = [[410, 310]]

for coord in crowns_coord:
    crown = Crown(coord[0], coord[1])
    crowns_list.add(crown)
    all_sprite_list.add(crown)

monsters_list = pygame.sprite.Group()
monster_coord = [[1, 500], [400, 50]]
'''добавляем данные об монстрах в список монстров и список спрайтов'''
for coord in monster_coord:
    monster = Monster(coord[0], coord[1])
    monsters_list.add(monster)
    all_sprite_list.add(monster)

'''указываем начальное положение персонажа игрока и добавлаяем и все элементы игры связываем с игроком,
дабы работало взаимодействие'''
player = Player(0, 15)
player.walls = wall_list
'''добавленяем спрайт персонажа игрока в список спрайтов'''
all_sprite_list.add(player)



player.diamonds = diamonds_list
player.monsters = monsters_list
player.crowns = crowns_list

'''Если игра завершена, на экране показываем текст с завершением игры'''
font = pygame.font.SysFont('Calibri', 150, True)
text = font.render('You Dead', True, RED)
text1 = font.render('Win!', True, WHITE)
'''Запуск игры. Добавляем таймер'''
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        '''если игра завершается, то мы больше ничего не делаем'''
        if event.type == pygame.QUIT:
            done = True
        #если мы запускаем движение, то меняем координаты персонажа игрока
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.change_x = 3
            elif event.key == pygame.K_a:
                player.change_x = -3
            elif event.key == pygame.K_w:
                player.change_y = -3
            elif event.key == pygame.K_s:
                player.change_y = 3
        #если мы прекращаем движение, то не меняем координаты персонажа игрока
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.change_x = 0
            elif event.key == pygame.K_a:
                player.change_x = 0
            elif event.key == pygame.K_w:
                player.change_y = 0
            elif event.key == pygame.K_s:
                player.change_y = 0

    '''весь фон игры цвета PURPLE'''
    screen.fill(PURPLE)
    '''если персонаж умер, что выводим текст'''
    if not player.alive:
        screen.blit(text, (100,10))
    #если это не произошло, то игра продолжается и обновляется
    else:
        all_sprite_list.update()
        all_sprite_list.draw(screen)

    if player.collected_crowns == 1 and player.alive and player.collected_diamonds ==3:
        screen.blit(text1, (240, 220))




    if player.collected_crowns == 1:
        all_sprite_list.update()






    '''Запуск дисплея игры'''
    pygame.display.flip()
    clock.tick(60)

'''выходим из игры'''
pygame.quit()






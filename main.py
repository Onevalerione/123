import pygame
import sys
from Player import player


Purple = (51, 0, 51)
White = (0, 0, 0)
fps = 30


def run():

    '''инициализируем игру'''
    pygame.init()

    '''создаем отображаемую область для игры'''
    screen = pygame.display.set_mode((800, 600))
    ''''задаем название отображаемой области'''
    pygame.display.set_caption('Лабиринт')
    bg_color = (Purple)
    wall_color = (White)
    Player = player(screen)


    '''создаем список спрайтов для нашей игры и включаем в нее спрайт стен'''
    all_sprite_list = pygame.sprite.Group()
    wall_list = pygame.sprite.Group()

    '''список стен [координата x, координата y, ширина, высота]'''
    wall_crds = [
        [0, 0, 10, 600],
        [790, 0, 10, 600],
        [0, 0, 790, 10],
        [0, 590, 600, 10]
    ]

    '''создаем список ключей в списке спрайтов игры и устанавливаем координаты ключей'''
    keys_list = pygame.sprite.Group()
    keys_list = [[750,50]]


    '''Созданием новый класс для игрока'''







    class Wall(pygame.sprite.Sprite):
        '''класс, который будет создавать стены, в качестве преграды по указанным координатам и размерам'''

        def __init__(self, x, y, width, height):
            super().__init__()

            self.img = pygame.Surface([width, height])
            self.img.fill(wall_color)

            self.rect = self.img.get_rect()
            self.rect.x = x
            self.rect.y = y

    class Keys(pygame.sprite.Sprite):
        '''класс, который загрузит изображение ключа в спрайты'''
        def __int__(self, x, y, img='P1.png'):
            super().__init__()
            self.image = pygame.image.load(img).convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    '''добавляем список стен в список спрайтов стен и общий список спрайтов'''
    for crds in wall_crds:
        wall = Wall(crds[0], crds[1], crds[2], crds[3])
        wall_list.add(wall)
        all_sprite_list.add(wall)

    '''добавлем координаты ключей в список ключей и список спрайтов'''
    for crds in keys_list:
        key = Keys(crds[0], crds[1])
        keys_list.add(key)
        all_sprite_list.add(key)

    '''Создаем бесконечный цикл, в котором будут содержаться все события в игре'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        Player.output()
        pygame.display.flip()


run()

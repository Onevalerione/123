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

    '''добавляем список стен в список спрайтов стен и общий список спрайтов'''
    for crd in wall_crds:
        wall = Wall(crd[0], crd[1], crd[2], crd[3])
        wall_list.add(wall)
        all_sprite_list.add(wall)

    '''Создаем бесконечный цикл, в котором будут содержаться все события в игре'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        Player.output()
        pygame.display.flip()


run()

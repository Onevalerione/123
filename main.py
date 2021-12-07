import pygame
import sys


Purple = (51, 0, 51)

def run():


    '''инициализируем игру'''
    pygame.init()

    '''создаем отображаемую область для игры'''
    screen = pygame.display.set_mode((800, 600))
    ''''задаем название отображаемой области'''
    pygame.display.set_caption('Лабиринт')
    bg_color = (Purple)

    '''Создаем бесконечный цикл, в котором будут содержаться все события в игре'''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()


run()







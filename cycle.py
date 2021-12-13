import pygame
import sys

def events(Player):
    '''Обрабатываем события'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            '''Вправо'''
            if event.key == pygame.K_d:
                Player.mright = True
                '''Влево'''
            elif event.key == pygame.K_a:
                Player.mleft = True
                '''Вверх'''
            elif event.key == pygame.K_w:
                Player.mtop = True

        elif event.type == pygame.KEYUP:
            '''Вправо'''
            if event.key == pygame.K_d:
                 Player.mright = False
                 '''Влево'''
            elif event.key == pygame.K_a:
                Player.mleft = False
                '''Вверх'''
            elif event.key == pygame.K_w:
                Player.mtop = False





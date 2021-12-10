import pygame



class player():

    def __init__(self, screen):
        '''инициализируем игрока'''
        self.screen = screen
        self.image = pygame.image.load('P1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def output(self):
        '''выводим изображение игрока на экран'''
        self.screen.blit(self.image, self.rect)

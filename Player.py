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
        self.mright = False
        self.mleft = False
        self.mtop = False

    def output(self):
        '''выводим изображение игрока на экран'''
        self.screen.blit(self.image, self.rect)

    def update_Player(self):
        '''обновление позиции пушки'''
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= 1
        if self.mtop and self.rect.top < self.screen_rect.top:
            self.rect.centery += 1










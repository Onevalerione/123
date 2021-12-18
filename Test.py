import pygame
import unittest
WIDTH = 800
HEIGHT = 600
PURPLE = (51, 0, 51)
from pygame import display


'''Проверяем параметры экрана и их работу'''
class DisplayModuleTest(unittest.TestCase):
    default_caption = "pygame window"

    def setUp(self):
        display.init()

    def tearDown(self):
        display.quit()

    def test_update(self):
        #Проверяем, что последовательность типов событий может быть заблокирована
        screen = pygame.display.set_mode([WIDTH,HEIGHT])
        screen.fill(PURPLE)

        r1 = pygame.Rect(0, 0, 100, 100)
        pygame.display.update(r1)

        r2 = pygame.Rect(-10, 0, 100, 100)
        pygame.display.update(r2)

        r3 = pygame.Rect(-10, 0, -100, -100)
        pygame.display.update(r3)

    def test_set_blocked__event_sequence(self):
        event_types = [
            pygame.KEYDOWN,
            pygame.KEYUP

        ]

        pygame.event.set_blocked(event_types)

    def test_flip(self):
        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        # Тест без изменений
        self.assertIsNone(pygame.display.flip())

        # Тест с изменениями
        pygame.Surface.fill(screen, (PURPLE))
        self.assertIsNone(pygame.display.flip())

        # Тест без инициализации дисплея
        pygame.display.quit()
        with self.assertRaises(pygame.error):
            (pygame.display.flip())

        # Тест без окна
        del screen
        with self.assertRaises(pygame.error):
            (pygame.display.flip())


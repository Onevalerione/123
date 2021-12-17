
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

        screen = pygame.display.set_mode([WIDTH,HEIGHT])
        screen.fill(PURPLE)

    def test_set_blocked__event_sequence(self):
        """Ensure a sequence of event types can be blocked."""
        event_types = [
            pygame.KEYDOWN,
            pygame.KEYUP

        ]

        pygame.event.set_blocked(event_types)
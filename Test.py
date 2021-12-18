import pygame
import unittest
WIDTH = 800
HEIGHT = 600
PURPLE = (51, 0, 51)
from pygame import display
from main import Player
from main import Monster
from main import Crown
from main import Diamond

'''Проверяем параметры экрана и их работу'''
class DisplayModuleTest(unittest.TestCase):
    default_caption = "pygame window"

    def setUp(self):
        display.init()

    def tearDown(self):
        display.quit()

    def test_update(self):
        #Проверка движения объектов
        screen = pygame.display.set_mode([WIDTH,HEIGHT])
        screen.fill(PURPLE)

        r1 = pygame.Rect(0, 0, 100, 100)
        pygame.display.update(r1)

        r2 = pygame.Rect(-10, 0, 100, 100)
        pygame.display.update(r2)

        r3 = pygame.Rect(-10, 0, -100, -100)
        pygame.display.update(r3)

    def test_set_blocked__event_sequence(self):
        # Проверяем, что последовательность типов событий может быть заблокирована
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

class Player_Tests(unittest.TestCase):
    def test_player_die(self):
        pygame.init()
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        virus_list = pygame.sprite.Group()
        wall_list = pygame.sprite.Group()
        crowns_list = pygame.sprite.Group()
        monsters_list = pygame.sprite.Group()
        diamonds_list = pygame.sprite.Group()
        player = Player(110,80)
        monster = Monster(110, 80)
        monsters_list.add(monster)
        player.diamonds = diamonds_list
        player.monsters = monsters_list
        player.walls = wall_list
        player.crowns = crowns_list
        player.virus = virus_list
        player.update()
        self.assertFalse(player.alive)

#Проверим что корона исчезает при взаимодействии с игроком
    def test_collect_crown(self):
        pygame.init()
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        virus_list = pygame.sprite.Group()
        wall_list = pygame.sprite.Group()
        crowns_list = pygame.sprite.Group()
        monsters_list = pygame.sprite.Group()
        diamonds_list = pygame.sprite.Group()
        player = Player(410, 310)
        crown = Crown(410, 310)
        crowns_list.add(crown)
        player.diamonds = diamonds_list
        player.monsters = monsters_list
        player.walls = wall_list
        player.crowns = crowns_list
        player.virus = virus_list
        player.update()
        self.assertFalse(crown.kill())

# Проверим что алмаз исчезает при взаимодействии с игроком
    def test_diamond_kill(self):
        pygame.init()
        screen = pygame.display.set_mode([WIDTH, HEIGHT])
        virus_list = pygame.sprite.Group()
        wall_list = pygame.sprite.Group()
        crowns_list = pygame.sprite.Group()
        monsters_list = pygame.sprite.Group()
        diamonds_list = pygame.sprite.Group()
        player = Player(110,80)
        diamond = Diamond(110, 80)
        player.diamonds = diamonds_list
        player.monsters = monsters_list
        player.walls = wall_list
        player.crowns = crowns_list
        player.virus = virus_list
        player.update()
        self.assertFalse(diamond.kill())



if __name__ == '__main__':
    pygame.init()




import functions
import objects
import pygame
import objects
import sys


class Game:
    def __init__(self, size: tuple, map_name: str):
        pygame.init()
        self.width = size[0]
        self.height = size[1]
        self.towers = []
        self.units = pygame.sprite.Group()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.map_name = map_name

    def run(self):
        run = True
        clock = pygame.time.Clock()
        self.screen.fill((0, 0, 0))
        self._select_track(map_name=self.map_name)
        self._build_track()
        self._spawn_footman()

        while run:

            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()


                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pos)
                    pass

            self._build_track()
            self.f1.move()
            self.f1.draw(self.screen)
            # print(self.f1.alive())
            # self.f1.update()

            pygame.display.flip()

    def _spawn_footman(self):
        self.f1 = objects.Footman('default_map')
        self.f1.add(self.units)

    def _select_track(self, map_name: str=''):
        if map_name == '':
            raise ValueError("Track name not specified")

        self.track = functions.load_track(name=map_name)

    def _build_track(self):
        self.screen.blit(self.track, (0, 0))
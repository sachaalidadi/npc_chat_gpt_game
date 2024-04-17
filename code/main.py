import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
          
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()

        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        # main_sound.play(loops=-1)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if self.level.level_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            self.level.toggle_menu()
                else:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.level.level_active = True
            if self.level.level_active:
                self.screen.fill(WATER_COLOR)
                self.level.run()
            else:
                self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)

 
if __name__ == '__main__':
    game = Game()
    game.run()
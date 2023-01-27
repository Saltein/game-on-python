import pygame
from consts import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    # Функция обновения спрайта   

    def update(self):


            # Движение
        def move_left(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                self.rect.x -= PLAYER_SPEED

        def move_up(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.rect.y -= PLAYER_SPEED
            
        def move_right(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                self.rect.x += PLAYER_SPEED

        def move_down(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                self.rect.y += PLAYER_SPEED

        move_left(self)
        move_up(self)
        move_right(self)
        move_down(self)
        
        
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0         # если левая сторона rect пропадает с экрана, просто задаем значение правого края равное 0
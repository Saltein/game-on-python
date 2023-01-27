import pygame
from consts import *
from classes import *

            # Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


# Вот как нужно создавать группу спрайтов в игре
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

# Добавить спрайт в группу
player = Player()
all_sprites.add(player)


            # Цикл игры
running = True
while running:
    
    for event in pygame.event.get():   # Ввод процесса (события)
        if event.type == pygame.QUIT:  # check for closing window
            running = False

    # Обновление спрайтов
    all_sprites.update() 

    # отрисовка
    screen.fill(BLACK) # закраштвает фон
    all_sprites.draw(screen) # рисует спрайты
    
    clock.tick(FPS)  # Держим цикл на правильной скорости
    pygame.display.flip()  # После отрисовки всего, переворачиваем экран

pygame.quit()
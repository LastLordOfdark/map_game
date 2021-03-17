"""
Главный скрипт запуска
"""
import pygame
import map_game.database

def run():
    WIDTH = 360  # ширина игрового окна
    HEIGHT = 480 # высота игрового окна
    FPS = 30 # частота кадров в секунду
    BLACK = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    db = map_game.database.DataBase()
    data = db.load()

    # Цикл игры
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            # проверить закрытие окна
            if event.type == pygame.QUIT:
                running = False
        # Рендеринг
        screen.fill(BLACK)
        pygame.draw.polygon(screen, (160, 160, 160), [(20, 20), (40, 20), (40, 40),(20, 40) ], 0)
        pygame.draw.lines(screen, (60, 255, 60), False, [(100, 100), (100, 150), (150, 150)], 5)
        # после отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    run()
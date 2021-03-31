"""
Главный скрипт запуска
"""
import pygame
import map_game.database
import map_game.graphics import Polygon, Srteet

def run():
    WIDTH = 360  # ширина игрового окна
    HEIGHT = 480 # высота игрового окна
    FPS = 30 # частота кадров в секунду
    BLACK = (0, 0, 0)

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("My Game")
    clock = pygame.time.Clock()

    house_sprites, area_sprites, road_sprites = init_sprites()

    running = init_sprites()
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


def init_sprites():
    db = map_game.database.DataBase()
    data = db.load()
    # Цикл игры
    running = True
    points = data['Points']
    houses = data['Houses']
    areas = data['Areas']
    roads = data['Roads']
    house_sprites = pygame.sprite.Group()
    area_sprites = pygame.sprite.Group()
    road_sprites = pygame.sprite.Group()
    for house in houses:
        p = Polygon(house, points)
        p.fill_surface()
        house_sprites.add(p)
    for area in areas:
        p = Polygon(areas, points)
        p.fill_surface()
        area_sprites.add(p)
    for road in roads:
        road_sprites.add(Road(road, points))

    return house_sprites, area_sprites, road_sprites


if __name__ == '__main__':
    run()
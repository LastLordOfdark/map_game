import pygame

BLACK = (0, 0, 0)


class Ground(pygame.sprite.Sprite):
    def __init__(self, data, points):
        super().__init__()
        self.color = data.color
        self.screen_coord = self.convert_coord(data, points)
        dimension, min_coord = self.get_dimension(self.screen_coord)
        self.image = pygame.Surface(dimension)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = dimension[0]//2 + min_coord[0]
        self.rect.centery = dimension[1] // 2 + min_coord[1]
        self.shift_coordinates(*min_coord)
        pass

    def shift_coordinates(self, x_min, y_min):
        self.screen_coord = [(x - x_min, y - y_min)
                             for (x, y) in self.screen_coord]

    def convert_coord(self, data, points):
        points_ = [points[p] for p in data.points]
        screen_coord = [(p.x, p.y) for p in points_]
        return screen_coord

    def get_dimension(self, coords):
        x = [c[0] for c in coords]
        y = [c[1] for c in coords]
        diff_x = abs(max(x) - min(x))
        diff_y = abs(max(y) - min(y))
        return  (diff_x, diff_y), (min(x), min(y))


class Polygon(Ground):
    def fill_surface(self):
        pygame.draw.polygon(self.image, self.color, self.screen_coord, 0)


class Road(Ground):
    def __init__(self, data, points):
        super().__init__(data, points)
        self.width = data.width

    def fill_surface(self):
        pygame.draw.lines(self.image, self.color, False, self.screen_coord, self.width)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.color = (255, 255, 255)
        self.image = pygame.Surface((20,20))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.keys = {'up': False, 'down': False, 'left': False, 'right': False}

    def move(self, keys_down, keys_up):
        for d in ['down', 'up', 'left', 'right']:
            if keys_down[d]:
                self.keys[d] = True
            if keys_up[d]:
                self.keys[d] = False

        if self.keys['down']:
            self.rect.centery += 3
        elif self.keys['up']:
            self.rect.centery -= 3
        elif self.keys['left']:
            self.rect.centerx -= 3
        elif self.keys['right']:
            self.rect.centerx += 3
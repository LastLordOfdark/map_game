import pickle
from collections import namedtuple


Point = namedtuple('Point', 'x y')
Road = namedtuple('Road', 'points widht color')
Area = namedtuple('Area', 'points color can_cross')


class Database:
    def __init__(self):
        self.FILENAME = 'map_base.data'
        self.db = {
            'Points': {},
            'Roads': {},
            'Houses': {},
            'Areas': {}
        }

    def save(self, data: dict):
        packed_data = self._pack(data)
        with open('data.pickle', 'wb') as f:
            pickle.dump(packed_data, f)

    def load(self):
        ...

    def _pack(self, data: dict):
        self._make_points(data['nodes'])
        for way in data['ways']:
            if self._check_loop(way):
                self._make_area(way)
            else:
                self._make_road(way)
        return self.db

    def _make_points(self, data: list):
        lon = []
        lat = []
        K = 100000
        for point in data:
            # = latitude - широта    (y)
            # = longitube - долгота  (x)
            lon.append(float(point.lon))
            lat.append(float(point.lat))
        dx = max(lon) - min(lon)
        dy = max(lat) - min(lat)
        min_lon = min(lon)
        min_lat = min(lat)
        for point in data:
            x = int((float(point.lon) - min_lon) * K)
            y = int((float(point.lat) - min_lat) * K)
            idx = int(point.id)
            self.db['Points'][idx] = Point(x, y)


    def _check_loop(self, way):
        "Проверяет замкнут ли путь"
        return way.nds[0] == way.nds[-1]


    def _make_area(self, way):
        "Создать объект здания или площади на местности"
        idx = int(way.id)
        points = [int(i) for i in way.nds]
        for tag in way.tags:
            if tag.k == 'building':
                key = 'Houses'
                color = (0, 255, 0)
                can_cross = False
            else:
                key = 'Areas'
                color = (0, 255, 0)
                can_cross = True
        self.db[key][idx] = Area(points, color, can_cross)


    def _make_road(self, way):
        "Создать дорогу"
        idx = int(way.id)
        width = 3
        color = (255, 0, 0)
        points = [int(i) for i in way.nds]
        self.db['Roads'][idx] = Road(points, width, color)

def create():
    return DataBase()
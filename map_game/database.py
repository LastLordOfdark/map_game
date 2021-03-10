from collections import namedtuple


Point = namedtuple('Point', 'x y')


class Database:
    def __init__(self):
        self.FILENAME = 'map_base.data'


    def save(self, data: dict):
        packed_data = self._pack(data)

    def load(self):
        ...

    def _pack(self, data: dict):
        self._make_points(data['nodes'])
        for way in data['ways']:
            is self._check_loop(way):
                self._make_road(way)






    def _make_points(self, data: list):
        lon = []
        lat = []
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
        ...


    def _make_road(self, way):
        "Создать дорогу"
        ...



def create():
    return DataBase()


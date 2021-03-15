"""
Тестирование загрузчика данных
"""
import map_game.loader
import map_game.database


def test_parser():
    FILENAME = 'map.xml'
    result = map_game.loader._load(FILENAME)
    parsed = map_game.loader.parser(result)
    db = map_game.database.Database()
    packed = db._pack(parsed)
    assert packed['Points']
    assert packed['Roads']
    assert packed['Houses']
    assert packed['Areas']
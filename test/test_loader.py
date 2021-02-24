"""
Тестирование загрузчика данных
"""
import map_game.loader

def test_parser():
    FILENAME = 'map.xml'
    result = map_game.loader._load(FILENAME)
    parsed = map_game.loader.parser(result)
    assert 'nodes' in result
    assert 'ways' in result

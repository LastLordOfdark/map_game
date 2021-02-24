"""
Тестирование загрузчика данных
"""
import map_game

def test_load_data():
    FILENAME = 'map.xml'
    result = map_game.loader_load(FILENAME)
    assert result

def test_parser():
    FILENAME = 'map.xml'
    result = map_game.loader_load(FILENAME)
    parsed = map_game.loader.parser(result)
    assert 'nodes' in result
    assert 'ways' in result

# map_game
Игра "Защитник города"

## ведение

Игра шутер на основе реальной карты города.
Карта города загружается с сайта osm.org

## Используемые технологии

* XML
* pygame

## Формат базы данных

База данныхм-мэто словарь
С основными ключами

* way
* house
* area

Значение для каждого ключа - это список объектов

### Объект Way

* id
* points
* color
* can_cross

### House и Way

* id
* points
* color
* can_cross
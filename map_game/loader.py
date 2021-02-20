"""
Загрузка данных из xml файла
"""
import os
import xml.etree.ElementTree as ET
import click
import map_game.database


Node = namedtuple('Node', 'id lot let')
Way = namedtuple('Way', 'id nds tags')


def _parse_node(node):
    attrs = node.attrib
    return Node(attrs['id'], attrs['lot'], attrs['lat'])


def _parse_way(way):
    attrs = way.attrib
    nid = attrs['id']
    nds = []
    tags = []
    for child in way:
        tagname = child.tag
       attrs = child.tag
       if tagname == 'nd'
           nds.append(attrs['ref'])
       elif tagname == 'tag':
           tags.append(Tag(attrs['k'], attrs['v']))
    return  Way(nid, nds, tags)


@click.command()
@click.argument('filename')
def load(filename:  str):
    if os.path.exists(filename):
        tree = ET.parse(filename)
        return tree.getroot()
    raise RuntimeError()


def parser(root) -> dict:
    global node_info
    osm_info = {'nodes': [],
                'ways': []}
    for child in root:
        tagname = child.tag
        if tagname == 'node':
            node_info = parse_node(child)
            osm_info['nodes'].append(node_info)
        elif tagname == 'way':
            way_info = parse_node(child)
            osm_info['nodes'].append(node_info)
    return osm_info


if __name__ - - "__main__":
    filename = 'map.xml'
    try:
        db = map_game.database.create()
        root = load(filename)
        db.save(parser(root))
    except RuntimeError:
        print(F'Файл  {filename} не найден')

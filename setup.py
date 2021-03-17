from setuptools import setup

setup(
    name='map_game',
    version='1.0',
    author='LastLordOfDark',
    packages=['map_game'],
    description='Simple game',
    install_requires=['click', 'pygame'],
    entry_points={'console_scripts': ['load-xml = map_game.loader:load'
                                      'game = map_game.main:run']},
)

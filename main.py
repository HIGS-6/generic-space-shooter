# Generic Space Shooter
from tito_engine.gui.text import Text
from custom_objs.player import Player
from custom_objs.enemy import Enemy
from random import uniform
from tito_engine import *

player = Player(
    8.0, 25.0, 0.5, ['Enemy', 'Asteroid'], 150.0, path_to_img='assets/sprites/playerShip2_orange.png',
    tag='Player'
)

text = Text('Hello World!', 'Comic Sans MS', 50, tag='Label')


enemies = [
    Enemy(
        2.0,
        25.0,
        3,
        ['Player'],
        50.0,
        'assets/sprites/Enemies/enemyGreen1.png',
        Transform(
            Vec2(uniform(50.0, 1000.0), uniform(50.0, 100.0)),
            uniform(0.0, 360.0),
            scale=1,
        ),
        tag='Enemy'
    )
    for _ in range(5)]


TitoEngine(colour_fill=(40, 32, 51)).run([player, text, *enemies])

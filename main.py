# Generic Space Shooter
from custom_objs.enemy import Enemy
from custom_objs.player import Player
from random import uniform
from tito_engine import *

player = Player(
    5.0, 20.0, 0.25, ['Enemy', 'Asteroid'], path_to_img='assets/sprites/playerShip2_orange.png',
    tag='Player'
)


enemies = [
    Enemy(
        2.5,
        20.0,
        3,
        ['Player'],
        'assets/sprites/Enemies/enemyGreen1.png',
        Transform(
            Vec2(uniform(50.0, 1000.0), uniform(50.0, 100.0)),
            uniform(0.0, 360.0),
            scale=1,
        ),
        tag='Enemy'
    )
    for _ in range(5)]


TitoEngine(colour_fill=(40, 32, 51)).run([player, *enemies])

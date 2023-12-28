# Generic Space Shooter
from custom_objs.spaceship import SpaceShip
from custom_objs.enemy import EnemySpaceship
from random import uniform
from tito_engine import *

player = SpaceShip(
    5.0, 1.0, path_to_img='assets/sprites/playerShip2_orange.png',
    transform=Transform(Vec2(30, 360), 0, 1),
    tag='Player'
)


enemies = [
    EnemySpaceship(
        2.5,
        20.0,
        170,
        'assets/sprites/Enemies/enemyGreen1.png',
        Transform(
            Vec2(uniform(50.0, 500.0), uniform(50.0, 500.0)),
            uniform(0.0, 360.0),
            scale=1,
        ),
        tag='Enemy'
    )
    for _ in range(2)]


TitoEngine(colour_fill=(40, 32, 51)).run([player, *enemies])

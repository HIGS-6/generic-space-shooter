from custom_objs.top_down_character import TapToMoveCharacterController
from custom_objs.zombie import Zombie
from random import uniform
from tito_engine import *

player = TapToMoveCharacterController(
    4.0, path_to_img='assets/sprites/survivor.png',
    transform=Transform(Vec2(30, 360)),
    tag='Player'
)


zombies = [
    Zombie(
        uniform(1.5, 3.25),
        20.0,
        uniform(150.0, 350.0),
        'assets/sprites/zombie.png',
        Transform(
            Vec2(uniform(50.0, 1000.0), uniform(50.0, 1000.0)),
            uniform(0.0, 360.0),
            scale=uniform(1.0, 1.25),
        ),
    )
for _ in range(10)]


TitoEngine(colour_fill=(40, 40, 40)).run([player, *zombies])
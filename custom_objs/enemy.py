from tito_engine import Sprite, Transform, Vec2, World
from pygame.sprite import collide_circle


class EnemySpaceship(Sprite):
    def __init__(self, move_speed: float, damage: float, field_of_view: float, path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        self.move_speed = move_speed
        self.damage = damage
        super().__init__(path_to_img, transform, enabled, tag)
        self.radius = field_of_view

    def update(self, world: World):
        player = world.find_obj_by_tag('Player')

        if collide_circle(player, self) and Vec2.distance(player.transform.position, self.transform.position) > 35:
            self.transform.look_at(player.transform.position)
            self.transform.position += self.transform.forward() * self.move_speed

        super().update(world)

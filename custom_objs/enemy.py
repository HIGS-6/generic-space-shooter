from tito_engine import Transform, Vec2, World
from custom_objs.spaceship import Spaceship
# from pygame.sprite import collide_circle


class Enemy(Spaceship):
    def __init__(self, speed: float, damage: float, shoot_cooldown: float, target_tags: list[str], path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        super().__init__(speed, damage, shoot_cooldown,
                         target_tags, path_to_img, transform, enabled, tag)
        self._min_shooting_distance = 500

    def update(self, world: World):
        player = world.find_obj_by_tag('Player')

        if player:
            if Vec2.distance(player.transform.position, self.transform.position) > self._min_shooting_distance:
                self.transform.position += self.transform.forward() * self._speed
            else:
                # Close Enough to Open Fire
                self.shoot(world)

            self.transform.look_at(player.transform.position)

            self.shooting_cooldown(world)
        

        super().update(world)

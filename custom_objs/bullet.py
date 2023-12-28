from tito_engine.sprite import Sprite
from tito_engine.transform import Transform
from pygame.rect import Rect


class Bullet(Sprite):
    def __init__(self, life_time: float, speed: float, target_tag: str, path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        super().__init__(path_to_img, transform, enabled, tag)
        self._travel_speed = speed
        self._life_time = life_time
        self._target_tag = target_tag
    
    def update(self, world):
        super().update(world)

        # Go Forward
        self.transform.position += self.transform.forward() * self._travel_speed

        # Check for collisions:
        targets: list[Sprite] = world.find_objs_by_tag(self._target_tag)
        for target in targets:
            if self.rect.colliderect(target.rect):
                # When we hit the target we destroy it spawn a VFX, Play a sound and destroy ourselfs
                # TODO: THAT                 ^^^
                world.destroy(target)
                world.destroy(self)
                return
                # del self

        # Update Life Time
        self._life_time -= world.dt
        if self._life_time < 0:
            world.destroy(self)


from tito_engine.sound_manager import SoundManager
from tito_engine.transform import Transform
from tito_engine.sprite import Sprite
from tito_engine.world import World


class Bullet(Sprite):
    def __init__(self, life_time: float, speed: float, target_tags: list[str], path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        super().__init__(path_to_img, transform, enabled, tag)
        self._travel_speed = speed
        self._life_time = life_time
        self._target_tags = target_tags

    def update(self, world: World):
        super().update(world)
        # Go Forward
        self.transform.position += self.transform.forward() * self._travel_speed

        # print(f'Targets: {self._target_tags}')
        # Check for collisions:
        targets: list[Sprite] = world.find_objs_by_tags(self._target_tags)
        # print(targets)
        for target in targets:
            if self.rect.colliderect(target.rect):
                print(f'Hit {target.tag}')
                # When we hit the target we destroy it, spawn a VFX, Play a SFX and destroy ourselfs
                # TODO: THAT                                 ^^^
                SoundManager.play_sound('assets/sfx/explosionCrunch_003.ogg')
                world.destroy(target)
                world.destroy(self)
                return

        # Update Life Time
        self._life_time -= world.dt
        if self._life_time < 0:
            world.destroy(self)
            return

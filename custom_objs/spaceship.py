from tito_engine.sound_manager import SoundManager
from tito_engine.transform import Transform
from tito_engine.sprite import Sprite
from custom_objs.bullet import Bullet
from tito_engine.world import World


class Spaceship(Sprite):
    def __init__(self, speed: float, damage: float, shoot_cooldown: float, target_tags: list[str], health_points: float, path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        super().__init__(path_to_img, transform, enabled, tag)
        self._hp = health_points
        self._speed = speed
        self._damage = damage
        self._shoot_cooldown = shoot_cooldown
        self._current_cool_down = self._shoot_cooldown
        self._target_tags = target_tags
        self._can_shoot = True

    def update(self, world):
        super().update(world)
        self.shooting_cooldown(world)
        if self._hp <= 0:
            SoundManager.play_sound('assets/sfx/explosionCrunch_003.ogg')
            world.destroy(self)

    def shooting_cooldown(self, world):
        # Run Float Timer only if we can not shoot
        if self._can_shoot:
            return

        self._current_cool_down -= world.dt

        if self._current_cool_down <= 0:
            self._can_shoot = True

            # Reset Float Timer
            self._current_cool_down = self._shoot_cooldown

    def shoot(self, world: World):
        if self._can_shoot:
            SoundManager.play_sound('assets/sfx/laserSmall_001.ogg')
            world.instantiate(
                Bullet(self._damage, 1.5, 10, self._target_tags, 'assets/sprites/Lasers/laserGreen11.png',
                       Transform(self.transform.position + (self.transform.forward() * 60), self.transform.rotation, 0.75)))
            self._can_shoot = False

    def deal_damage(self, damage: float):
        self._hp -= damage
        print(f'HP: {self._hp}', end='\r')

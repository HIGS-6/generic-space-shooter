from tito_engine.audio_source import AudioSource
from tito_engine.object_pool import ObjectPool
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

        # Object Pooling Set up
        self._shooting_sfxs = ObjectPool(
            AudioSource, 15, ('assets/sfx/laserSmall_001.ogg', 100.0, False, True))
        
        self._bullets = ObjectPool(Bullet, 15, (self._damage, 1.5, 900.0, self._target_tags, 'assets/sprites/Lasers/laserGreen11.png',
                                                Transform(scale=0.75)))

    def update(self, world):
        super().update(world)
        self.shooting_cooldown(world)
        if self._hp <= 0:
            AudioSource.play_quick('assets/sfx/explosionCrunch_003.ogg')
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

    def shoot(self):
        if self._can_shoot:
            # Shooting Cooldown
            self._can_shoot = False

            # Play SFX
            sfx = self._shooting_sfxs.get()
            sfx.play()

            # Instantiate Bullet Object
            bullet = self._bullets.get()

            # Changing Bullet Position and Rotation
            bullet.transform.rotation = self.transform.rotation
            bullet.transform.position = self.transform.position + \
                (self.transform.forward() * 60)

    def deal_damage(self, damage: float):
        self._hp -= damage

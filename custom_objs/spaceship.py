from tito_engine import Sprite, Transform, InputManager, Vec2
from custom_objs.bullet import Bullet
from tito_engine.world import World


class SpaceShip(Sprite):
    def __init__(self, move_speed: float, shoot_cooldown: float, path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        self._move_speed = move_speed
        self._shoot_cooldown = shoot_cooldown
        self._current_cool_down = self._shoot_cooldown
        super().__init__(path_to_img, transform, enabled, tag)
        self._target_pos = self.transform.position

    def update(self, world: World):
        # print(f'GameObjects In Game: {len(world.game_objects)}')
        self.detect_tap()
        self.move_towards_target()
        self.shoot(world)
        super().update(world)

    def move_towards_target(self):
        if Vec2.distance(self.transform.position, self._target_pos) > 5:
            # Face the Target Position
            self.transform.look_at(self._target_pos)

            # Move Towards the Target Position
            self.transform.position += self.transform.forward() * self._move_speed

    def detect_tap(self):
        if InputManager.get_mouse_button(0):
            self._target_pos = InputManager.get_mouse_pos()

    def shoot(self, world: World):
        # Run Float Timer
        # print(f'Float Timer (Cooldown): {self._current_cool_down}')
        self._current_cool_down -= world.dt
        if self._current_cool_down <= 0:
            world.instantiate(
                Bullet(1.5, 12.5, 'Enemy', 'assets/sprites/Lasers/laserGreen11.png',
                       Transform(self.transform.position + (self.transform.forward() * 60), self.transform.rotation, 0.75)))

            # Reset Float Timer
            self._current_cool_down = self._shoot_cooldown

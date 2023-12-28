from tito_engine import Transform, InputManager, Vec2
from custom_objs.spaceship import Spaceship
from tito_engine.world import World
from pygame.display import Info


class Player(Spaceship):
    def __init__(self, speed: float, damage: float, shoot_cooldown: float, target_tags: list[str], path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        super().__init__(speed, damage, shoot_cooldown, target_tags,
                         path_to_img, transform, enabled, tag)
        info = Info()
        self.transform.position = Vec2(info.current_h / 2, info.current_w / 2)
        self._target_pos = self.transform.position

    def update(self, world: World):
        # print(f'GameObjects In Game: {len(world.game_objects)}')
        self.detect_tap()
        self.move_towards_target(world)
        self.shooting_cooldown(world)
        # self.shoot(world)
        super().update(world)

    def move_towards_target(self, world):
        if Vec2.distance(self.transform.position, self._target_pos) > 5:
            # Face the Target Position
            self.transform.look_at(self._target_pos)

            # Move Towards the Target Position
            self.transform.position += self.transform.forward() * self._speed

        # Pew Pew!
        if len(world.find_objs_by_tags(self._target_tags)) > 0:
            self.shoot(world)

    def detect_tap(self):
        if InputManager.get_mouse_button(0):
            self._target_pos = InputManager.get_mouse_pos()

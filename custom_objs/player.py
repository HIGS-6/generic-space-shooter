from tito_engine import TitoEngine, Transform, InputManager, Vec2
from custom_objs.spaceship import Spaceship
from tito_engine.world import World
from pygame.display import Info


class Player(Spaceship):
    def __init__(self, speed: float, damage: float, shoot_cooldown: float, target_tags: list[str], health_points, path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        super().__init__(speed, damage, shoot_cooldown, target_tags, health_points,
                         path_to_img, transform, enabled, tag)
        info = Info()
        self.transform.position = Vec2(info.current_w / 2, info.current_h / 2)
        self._target_pos = self.transform.position

    def update(self, world: World):
        # print(f'HP: {self._hp}', end='\r')
        label = world.find_obj_by_tag('Label')

        # if self._hp > 0:
        #     label.text = f'HP: {self._hp}'
        # else:
        #     label.text = 'Game Over'

        label.text = f'FPS: {TitoEngine.FPS:.0f}'

        info = Info()
        label.transform.position = Vec2(
            info.current_w / 2, info.current_h - 100)

        self.detect_tap()
        self.move_towards_target(world)
        super().update(world)

    def move_towards_target(self, world):
        if Vec2.distance(self.transform.position, self._target_pos) > 5:
            # Face the Target Position
            self.transform.look_at(self._target_pos)

            # Move Towards the Target Position
            self.transform.position += self.transform.forward() * self._speed * world.dt

        # Pew Pew!
        if len(world.find_objs_by_tags(self._target_tags)) > 0:
            self.shoot()

    def detect_tap(self):
        if InputManager.get_mouse_button(0):
            self._target_pos = InputManager.get_mouse_pos()

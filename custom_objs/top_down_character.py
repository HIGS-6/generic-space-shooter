from tito_engine import Sprite, Transform, InputManager, Vec2
import pygame as pg


class TapToMoveCharacterController(Sprite):
    def __init__(self, move_speed: float, path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        self._move_speed = move_speed
        super().__init__(path_to_img, transform, enabled, tag)
        self._target_pos = self.transform.position

    def update(self, world):
        self.detect_tap()
        self.move_towards_target()
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

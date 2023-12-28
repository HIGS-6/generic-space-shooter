from pygame.transform import rotozoom
from pygame.image import load
from .game_object import GameObject
from .transform import Transform
from .utils import resource_path


class Sprite(GameObject):
    def __init__(self, path_to_img: str, transform: Transform = Transform(), enabled=True, tag: str = ''):
        super().__init__(transform, enabled, tag)
        self.original_img = load(resource_path(path_to_img))
        self.previous_rot = 0
        self.image = self.original_img

        self.image = rotozoom(
            self.original_img, self.transform.rotation, self.transform.scale
        )
        self.rect = self.image.get_rect(
            center=(self.transform.position.x, self.transform.position.y)
        )

    def update(self, world):
        if self.previous_rot != self.transform.rotation:
            self.previous_rot = self.transform.rotation
            self.image = rotozoom(
                self.original_img, self.transform.rotation, self.transform.scale
            )

        self.rect = self.image.get_rect(
            center=(self.transform.position.x, self.transform.position.y)
        )

        world.window.blit(self.image, self.rect)

    def is_outside_screen(self) -> bool:
        return (
            self.transform.position.x > self.win.get_size()[0]
            or self.transform.position.x < 0
            or self.transform.position.y > self.win.get_size()[1]
            or self.transform.position.y < 0
        )

from tito_engine.vec2 import Vec2
from .transform import Transform
from .sprite import Sprite


class PhysicSprite(Sprite):
    """
    # Sprite Class with Physics:
    - Gravity
    - Collisions
    """

    def __init__(self, path_to_img, gravity=10, transform: Transform = Transform(), enabled=True, tag: str = ''):
        super().__init__(path_to_img, transform, enabled, tag)
        self.gravity = gravity
        self.y_velocity = 0
        self.x_velocity = 0
        self.__current_objs = []

    def update(self, world):
        self.__update_current_objs(world.game_objects)
        self.apply_gravity()
        self.transform.position += Vec2(self.x_velocity, self.y_velocity)
        super().update(world)
    
    def __update_current_objs(self, game_objects: list):
        self.__current_objs = [go for go in game_objects]

    def apply_gravity(self):
        if self.y_velocity < 10:
            self.y_velocity += self.gravity

        self.transform.position.y += self.y_velocity

    def is_colliding_with_tag(self, tag: str) -> bool:
        for obj in self.__current_objs:
            if obj.tag == tag and self.rect.colliderect(obj.rect):
                return True
            else:
                return False

    def add_force(self):
        pass

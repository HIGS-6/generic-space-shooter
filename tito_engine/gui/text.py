from tito_engine.transform import Transform
from tito_engine.sprite import Sprite
from pygame.font import SysFont


class Text(Sprite):
    def __init__(self, text='Some Text', font_name='Arial', font_size=28, font_colour=(255, 255, 255), bg_colour=None, transform: Transform = Transform(), enabled=True, tag: str = ''):
        self.text = text
        self.size = font_size
        self.colour = font_colour
        self.bg_colour = bg_colour
        self._font = SysFont(font_name, font_size)
        self._surface = self._font.render(text, False, font_colour, bg_colour)
        super().__init__(self._surface, transform, enabled, tag)

    def update(self, world):
        self._surface = self._font.render(
            self.text, True, self.colour, self.bg_colour)
        self.image = self._surface
        super().update(world)

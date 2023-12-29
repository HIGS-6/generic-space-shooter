from tito_engine.transform import Transform
from .game_object import GameObject
from pygame.mixer import Sound
from .utils import resource_path


class AudioSource(GameObject):
    def __init__(self, path_to_file: str, volume: float = 100.0, loop: bool = False, disable_on_finish: bool = False, transform: Transform = Transform(), enabled=True, tag: str = ''):
        super().__init__(transform, enabled, tag)
        self._volume = volume
        self.loop = loop
        self._sound = Sound(resource_path(path_to_file))
        self._channel = None
        self._disable_on_finish = disable_on_finish

    def update(self, world):
        if self._disable_on_finish and not self.is_playing:
            self.enabled = False
        super().update(world)

    @property
    def is_playing(self):
        if self._channel is None:
            return True
        return self._channel.get_busy()

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, new_volume):
        self._volume = new_volume
        self._sound.set_volume(self._volume)

    def play(self):
        self._channel = self._sound.play(-1 if self.loop else 0)

    @staticmethod
    def play_quick(path_to_file: str, volume: float = 100.0):
        sound = Sound(resource_path(path_to_file))
        sound.set_volume(volume)
        sound.play()

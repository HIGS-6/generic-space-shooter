from .utils import resource_path
from pygame.mixer import Sound

class SoundManager:
    def play_sound(path_to_sound: str, loop: bool = False) -> None:
        Sound(resource_path(path_to_sound)).play(loops=loop)

    def get_sound(path_to_sound: str) -> Sound:
        return Sound(resource_path(path_to_sound))

    def play_music(path_to_music: str) -> str:
        pass
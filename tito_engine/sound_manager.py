from .utils import resource_path
from pygame.mixer import Sound

class SoundManager:
    def play_sound(path_to_sound: str, loop: bool = False) -> None:
        Sound(path_to_sound).play(loops=loop)

    def play_music(path_to_music: str) -> str:
        pass
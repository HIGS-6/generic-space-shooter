from .utils import resource_path
import pygame as pg


class Animation:
    def __init__(self, key_frame_img_paths: list[str], speed: float) -> None:
        self.key_frames = list(
            map(lambda frame_img_path: pg.image.load(resource_path(frame_img_path))), key_frame_img_paths)
    

from .transform import Transform


class GameObject:
    def __init__(self, transform: Transform = Transform(), enabled=True, tag: str = ''):
        self.transform = transform
        self.enabled = enabled
        self.tag = tag

    def update(self, world):
        pass

from .game_object import GameObject


class World:
    def __init__(self, window, initial_objects: list[GameObject] = []) -> None:
        self.window = window
        self.dt = 0
        self.__game_objects: list[GameObject] = initial_objects

    @property
    def game_objects(self) -> list[GameObject]:
        return self.__game_objects

    def find_obj_by_tag(self, tag: str = '') -> GameObject:
        return [obj for obj in self.__game_objects if obj.tag == tag][0]
    
    def find_objs_by_tag(self, tag: str = '') -> list[GameObject]:
        return [obj for obj in self.__game_objects if obj.tag == tag]

    def instantiate(self, new_object: GameObject) -> GameObject:
        self.__game_objects.append(new_object)

        return self.game_objects[self.game_objects.index(new_object)]
    
    def destroy(self, target_obj: GameObject) -> None:
        self.__game_objects.remove(target_obj)
    
    def update(self, dt):
        self.dt = dt
        for obj in self.__game_objects:
            if obj.enabled:
                obj.update(self)
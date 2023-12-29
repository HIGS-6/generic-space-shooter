class ObjectPool:
    def __init__(self, object_type: type, pool_size: int, constructor_args: tuple) -> None:
        self._constructor_args = constructor_args
        self._object_type = object_type
        self._pool = [self._create_copy()] * pool_size

    def _create_copy(self):
        copy = self._object_type.__new__(self._object_type)
        copy.__init__(*self._constructor_args)
        return copy

    def get(self):
        for av in self._pool:
            if not av.enabled:
                return av

        new_obj = self._create_copy()
        self._pool.append(new_obj)
        return new_obj

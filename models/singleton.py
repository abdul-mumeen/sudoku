class SudokuMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs) -> object:
        """
        This ensures that possible changes to the value of the `__init__` 
        argument do not affect the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]
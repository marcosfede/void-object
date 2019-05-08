__version__ = '0.1.0'


class Void:
    def __init__(self, *args, **kwargs):
        pass

    def __getattr__(self, *args, **kwargs):
        return self

    def __call__(self, *args, **kwargs):
        return self

    def __getitem__(self, *args, **kwargs):
        return self

    def __enter__(self, *args, **kwargs):
        return self

    def __exit__(self, *args, **kwargs):
        return None

    def __str__(self, *args, **kwargs):
        return 'Void'

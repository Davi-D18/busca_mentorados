from abc import ABC
from types import SimpleNamespace


class BaseSettings(ABC):
    NAME_ENVIRONMENT = "Base"

    def return_settings(self):
        settings = {}

        for cls in type(self).__mro__:
            if cls is object:
                continue

            for name, value in cls.__dict__.items():
                if name.startswith("_"):
                    continue
                if callable(value):
                    continue

                settings[name] = getattr(self, name)

        return SimpleNamespace(**settings)

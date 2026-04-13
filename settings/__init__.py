from decouple import config

from .development import DevelopmentSettings

env = config("ENVIRONMENT")

ENVIROMENTS = {
    DevelopmentSettings.NAME_ENVIRONMENT: DevelopmentSettings,
}


def get_settings(env: str):
    if env not in ENVIROMENTS:
        raise ValueError(
            f"Environment '{env}' não encontrado. Informe um ambiente válido: {list(ENVIROMENTS.keys())}"
        )

    return ENVIROMENTS[env]().return_settings()


settings = get_settings(env)

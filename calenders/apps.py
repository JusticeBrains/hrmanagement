from django.apps import AppConfig


class CalendersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'calenders'

    # def ready(self) -> None:
    #     import calenders.signals

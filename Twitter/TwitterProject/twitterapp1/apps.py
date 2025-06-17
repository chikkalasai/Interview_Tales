from django.apps import AppConfig


class Twitterapp1Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "twitterapp1"


    def ready(self):
        import twitterapp1.signals



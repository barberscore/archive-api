from django.apps import AppConfig


class RegistrationConfig(AppConfig):
    name = 'apps.registration'
    verbose_name = 'Registration Manager'

    def ready(self):
        return

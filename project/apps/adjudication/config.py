from django.apps import AppConfig


class AdjudicationConfig(AppConfig):
    name = 'apps.adjudication'
    verbose_name = 'Adjudication Manager'

    def ready(self):
        from apps.adjudication import signals
        return

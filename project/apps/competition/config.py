from django.apps import AppConfig


class CompetitionConfig(AppConfig):
    name = 'apps.competition'
    verbose_name = 'Contest Scoring Manager'

    def ready(self):
        from apps.competition import signals
        return

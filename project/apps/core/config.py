
# Django
from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'apps.core'
    verbose_name = 'Base'

    def ready(self):
        # import algoliasearch_django as algoliasearch

        # from .indexes import AwardIndex
        # Award = self.get_model('award')
        # algoliasearch.register(Award, AwardIndex)

        # from .indexes import ChartIndex
        # Chart = self.get_model('chart')
        # algoliasearch.register(Chart, ChartIndex)

        # from .indexes import GroupIndex
        # Group = self.get_model('group')
        # algoliasearch.register(Group, GroupIndex)

        # from .indexes import PersonIndex
        # Person = self.get_model('person')
        # algoliasearch.register(Person, PersonIndex)

        # from .indexes import ConventionIndex
        # Convention = self.get_model('convention')
        # algoliasearch.register(Convention, ConventionIndex)

        return

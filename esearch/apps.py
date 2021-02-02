from django.apps import AppConfig


class EsearchConfig(AppConfig):
    name = 'esearch'

    def ready(self):
        import esearch.signals

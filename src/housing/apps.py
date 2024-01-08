from django.apps import AppConfig

"""
    Specify the default auto field to use when creating models in this application.
    In this case, it is configured to use BigAutoField, which is an enhanced version
    of the auto field that supports larger values
    """
class HousingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'housing'

from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    layout = "horizontal"

class ReservationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reservation'

from .models import Films
from films.get_data_info import get_four_days


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        return context

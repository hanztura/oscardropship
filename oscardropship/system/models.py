from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):

    def __str__(self):
        first_name = self.first_name
        last_name = self.last_name
        ret = _('No name provided.')

        if first_name:
            ret = '{} {}'.format(first_name, last_name)
        return ret

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        first_name = self.first_name
        last_name = self.last_name
        ret = '{} {}'.format(first_name, last_name) if first_name else self.username

        return ret

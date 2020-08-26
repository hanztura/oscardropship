from oscar.apps.order.abstract_models import *

BaseAbstractOrderNote = AbstractOrderNote


class AbstractOrderNote(BaseAbstractOrderNote):
    class Meta:
        abstract = True
        app_label = 'order'
        verbose_name = _("Order Note")
        verbose_name_plural = _("Order Notes")

    def __str__(self):
        return "'%s' (%s)" % (self.message[0:50], self.x_user)

    @property
    def x_user(self):
        try:
            return self.user
        except TypeError:
            return 'None'

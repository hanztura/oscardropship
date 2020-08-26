from oscar.apps.payment.admin import *  # noqa

PaypalOrder = get_model('payment', 'PaypalOrder')

admin.site.register(PaypalOrder)

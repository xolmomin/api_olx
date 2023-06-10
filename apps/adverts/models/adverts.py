from django.db.models import CASCADE, CharField, Model, ForeignKey, SlugField, TextField, TextChoices, IntegerField, \
    BooleanField


class Advert(Model):
    class Status(TextChoices):
        ACTIVE = 'active', 'Faol'
        PENDING = 'pending', 'Kutayotgan'
        UNPAID = 'unpaid', "To'lanmagan"
        INACTIVE = 'inactive', 'Nofaol'
        CANCEL = 'inactive', 'Rad etilgan'

    title = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    status = CharField(max_length=25, choices=Status.choices)

    description = TextField()

    view_count = IntegerField(default=0)
    is_auto_reload = BooleanField(default=False)

    author_phone = CharField(max_length=25)
    author = ForeignKey('users.User', CASCADE, 'adverts')




'''


class CurrencyType(TextChoices):
    USD = 'usd', 'USD'
    UZS = 'uzs', 'SUM'

class PriceType(TextChoices):
    CASH = 'cash', 'Narx'
    EXCHANGE = 'exchange', 'Ayirboshlash'
    FREE = 'free', 'Tekin'


price = IntegerField(null=True, blank=True)
price_type = CharField(max_length=10, choices=PriceType.choices)
currency_type = CharField(max_length=5, choices=CurrencyType.choices)

'''
from django.db.models import JSONField, CASCADE, CharField, Model, ForeignKey, SlugField, TextField, TextChoices, IntegerField, \
    BooleanField, ImageField


class Advert(Model):
    class Status(TextChoices):
        ACTIVE = 'active', 'Faol'
        PENDING = 'pending', 'Kutayotgan'
        UNPAID = 'unpaid', "To'lanmagan"
        INACTIVE = 'inactive', 'Nofaol'
        CANCEL = 'cancel', 'Rad etilgan'

    title = CharField(max_length=255)
    slug = SlugField(max_length=255, unique=True)
    status = CharField(max_length=25, choices=Status.choices)

    description = TextField()

    view_count = IntegerField(default=0)
    is_auto_reload = BooleanField(default=False)

    author_phone = CharField(max_length=25)
    category = ForeignKey('adverts.Category', CASCADE)
    author = ForeignKey('users.User', CASCADE, 'adverts')

    @property
    def images(self):
        return self.advertimage_set.all()

    @property
    def params(self):
        return self.advertparam_set.all()


class AdvertParam(Model):  # TODO: complete
    advert = ForeignKey('adverts.Advert', CASCADE)
    key = CharField(max_length=255)  # CategoryParam dagi code ga teng
    name = CharField(max_length=55, blank=True)  # CategoryParam dagi label ga teng
    type = CharField(max_length=255)
    value = JSONField(default=dict)


class AdvertImage(Model):
    advert = ForeignKey('adverts.Advert', CASCADE)
    image = ImageField(upload_to='adverts/')

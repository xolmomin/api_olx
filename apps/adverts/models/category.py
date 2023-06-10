from django.db.models import CASCADE, CharField, Model, ForeignKey, SlugField, TextField, TextChoices, IntegerField, \
    BooleanField, ImageField
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = CharField(max_length=50, unique=True)
    max_images = IntegerField()
    icon = ImageField(upload_to='category/icon/', null=True, blank=True)
    is_business = BooleanField(default=False)
    parent = TreeForeignKey('self', CASCADE, 'children', null=True, blank=True)

    class MPTTMeta:
        order_insertion_by = ['name']


class Parameter(Model):
    category = ForeignKey('adverts.Category', C)
    code = SlugField(max_length=255)
    label = ''
    range = BooleanField(default=False)
    type = ''
    units = ''
    validation = ''
    values = ''

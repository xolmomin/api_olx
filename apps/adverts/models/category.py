from django.db.models import CASCADE, CharField, Model, ForeignKey, SlugField, TextChoices, IntegerField, \
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

    @property
    def parameters(self):
        return self.parameter_set.all()


class Parameter(Model):
    class Type(TextChoices):
        ENUM = 'enum', 'Enum'
        BOOL = 'bool', 'Bool'
        SALARY = 'salary', 'Salary'

    category = ForeignKey('adverts.Category', CASCADE)
    code = SlugField(max_length=255)
    label = CharField(max_length=55, blank=True)
    range = BooleanField(default=False)
    type = CharField(max_length=25, choices=Type.choices)

    @property
    def params(self):
        return self.paramvalue_set.all()


class ParamValue(Model):
    parameter = ForeignKey('adverts.Parameter', CASCADE)
    key = CharField(max_length=55)
    label = CharField(max_length=55)

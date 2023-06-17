from django.db.models import CASCADE, CharField, Model, ForeignKey, TextChoices, IntegerField, \
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
        return self.categoryparam_set.all()


class CategoryParam(Model):  # TODO: complete
    class Type(TextChoices):
        ENUM = 'enum', 'Enum'
        BOOL = 'bool', 'Bool'
        DIGIT = 'digit', 'Digit'
        SALARY = 'salary', 'Salary'
        HIDDEN = 'hidden', 'Hidden'

    category = ForeignKey('adverts.Category', CASCADE)
    code = CharField(max_length=255)
    label = CharField(max_length=55, blank=True)
    range = BooleanField(default=False)
    type = CharField(max_length=25, choices=Type.choices)

    @property
    def values(self):
        return self.categoryvalue_set.all()


class CategoryValue(Model):  # TODO: complete
    category_param = ForeignKey('adverts.CategoryParam', CASCADE)
    key = CharField(max_length=255)
    label = CharField(max_length=255)

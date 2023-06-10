from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField, CheckConstraint, Q, DateField, ImageField


class User(AbstractUser):
    phone = CharField(max_length=25, unique=True)
    balance = IntegerField(default=0)
    image = ImageField(upload_to='users/images/%Y/%m/%d/')
    birth_date = DateField(null=True, blank=True)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(balance__gte=0),
                name='check_balance',
            )
        ]

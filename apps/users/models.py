from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, IntegerField, CheckConstraint, Q


class User(AbstractUser):
    phone = CharField(max_length=25, unique=True)
    balance = IntegerField(default=0)

    class Meta:
        constraints = [
            CheckConstraint(
                check=Q(balance__gte=0),
                name='check_balance',
            )
        ]


from django.db.models import Model, OneToOneField, CASCADE


class Profile(Model):
    user = OneToOneField('users.User', CASCADE)

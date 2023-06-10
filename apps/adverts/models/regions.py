from django.db.models import Model, CharField, ForeignKey, CASCADE


class Region(Model):
    name = CharField(max_length=255)


class District(Model):
    name = CharField(max_length=255)
    region = ForeignKey('adverts.Region', CASCADE)

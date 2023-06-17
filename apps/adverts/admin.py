from django.contrib import admin

from adverts.models import Advert, AdvertParam


@admin.register(Advert)
class AdvertModelAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertParam)
class AdvertParamModelAdmin(admin.ModelAdmin):
    pass

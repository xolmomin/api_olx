from django.contrib import admin

from adverts.models import Advert, AdvertParam, Category


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Advert)
class AdvertModelAdmin(admin.ModelAdmin):
    pass


@admin.register(AdvertParam)
class AdvertParamModelAdmin(admin.ModelAdmin):
    pass

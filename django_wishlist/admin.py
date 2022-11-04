from django.contrib import admin

from . import models

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Wish)
class WishAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Gift)
class GiftAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

from . import models, utils

admin.site.site_header = f"Wishlist Admin Build:{utils.get_build_number()}"
admin.site.site_title = "Wishlist Admin"
admin.site.index_title = "Wishlist Admin"

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Wish)
class WishAdmin(admin.ModelAdmin):
    model = models.Wish
    list_display = ('title', 'order', 'visible', 'gifted', 'updated', 'created')

@admin.register(models.Gift)
class GiftAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin
from .models import Place, Images


class ImageInline(admin.TabularInline):
    model = Images


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

    class Meta:
        model = Place


admin.site.register(Place, PlaceAdmin)
admin.site.register(Images)

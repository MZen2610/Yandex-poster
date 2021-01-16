from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Images


class ImageInline(admin.TabularInline):
    model = Images

    readonly_fields = ("get_preview",)

    def get_preview(self, obj):
        return format_html('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width if obj.image.width < 200 else 200,
            height=obj.image.height if obj.image.height < 200 else 200,
        )
        )

    fields = ('title', 'image', 'get_preview', 'num',)


class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

    fields = ('title', 'description_short', 'description_long', 'lng', 'lat')

    class Meta:
        model = Place


admin.site.register(Place, PlaceAdmin)
admin.site.register(Images)

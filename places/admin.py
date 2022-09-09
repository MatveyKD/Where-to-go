from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image

    fields = ("image", "preview", "image_number")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="{}" height={} style="max-width: 200px; max-height: 200px;"/>'.format(
                obj.image.url,
                obj.image.width,
                obj.image.height,
            ))
        else:
            return ""

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

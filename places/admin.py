from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image

from adminsortable2.admin import SortableStackedInline, SortableAdminBase


class ImageStackedInline(SortableStackedInline):
    model = Image

    fields = [("image", "preview"), ("image_number")]
    readonly_fields = ("preview",)

    extra = 0

    def preview(self, obj):
        return format_html(
            '<img src="{image_url}" style="max-height: 200px;"/>',
            image_url=obj.image.url
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageStackedInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    pass

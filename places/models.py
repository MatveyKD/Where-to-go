from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="название места"
    )
    description_short = models.TextField(
        verbose_name="короткое описание места"
    )
    description_long = HTMLField(blank=True)

    lng = models.FloatField(verbose_name="долгота")
    lat = models.FloatField(verbose_name="широта")

    place_id = models.CharField(
        max_length=20,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = [
            "title",
            "description_short",
            "description_long",
            "lng",
            "lat",
            "place_id"
        ]

class Image(models.Model):
    place = models.ForeignKey(
        Place,
        related_name="images",
        verbose_name="место картинки",
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to="media",
        verbose_name="картинка",
        null=True
    )
    image_number = models.IntegerField(
        verbose_name="номер картинки",
        default=0,
        db_index=True
    )

    def __str__(self):
        return f"{self.image_number} {self.place.title}"

    class Meta:
        ordering = [
            "image_number"
        ]
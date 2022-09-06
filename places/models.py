from django.db import models


class Place(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="название места"
    )
    description_short = models.TextField(
        verbose_name="короткое описание места",
        blank=True,
        null=True
    )
    description_long = models.TextField(verbose_name="полное описание места")

    lng = models.FloatField(verbose_name="широта")
    lat = models.FloatField(verbose_name="долгота")

    place_id = models.CharField(
        max_length=20,
        null=True
    )

    def __str__(self):
        return self.title

class Image(models.Model):
    place = models.ForeignKey(
        Place,
        related_name="images",
        verbose_name="место картинки",
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        verbose_name="картинка",
        null=True
    )
    image_number = models.IntegerField(
        verbose_name="номер картинки",
        null=True
    )

    def __str__(self):
        return f"{self.image_number} {self.place.title}"

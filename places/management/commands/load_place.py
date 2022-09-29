import os
import json
import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from django.core.exceptions import MultipleObjectsReturned
from places.models import Place, Image


class Command(BaseCommand):
    help = "Loading place from json"

    def handle(self, *args, **options):
        try:
            if options["load_url"]:
                load_place(options["load_url"], url=True)
            elif options["load_dir"]:
                load_dir(options["path"])
            else:
                load_place(options["path"])
        except MultipleObjectsReturned:
            raise "Найдено несколько объектов вместо одного"

    def add_arguments(self, parser):
        parser.add_argument(
            "-p",
            "--path",
            action="store",
            help="Путь до json файла"
        )
        parser.add_argument(
            "-d",
            "--load_dir",
            action="store_true",
            help="Загрузить все .json файлы из папки"
        )
        parser.add_argument(
            "-u",
            "--load_url",
            action="store",
            help="Скачать .json по ссылке",
            required=False,
            default=False
        )


def load_place(file_path, url=False):
    if not url:
        with open(file_path, "rb") as file:
            content = json.load(file)
    else:
        response = requests.get(file_path)
        content = response.json()

    place, is_created = Place.objects.get_or_create(
        title=content["title"],
        lng=content["coordinates"]["lng"],
        lat=content["coordinates"]["lat"],
        defaults={
            "description_long": content.get("description_long", ""),
            "description_short": content.get("description_short", ""),
        }
    )
    if is_created:
        for index, img in enumerate(content["imgs"]):
            response = requests.get(img)
            Image.objects.create(
                place=place,
                image=ContentFile(response.content, f"{place.title}{index}.jpg"),
                image_number=index
            )


def load_dir(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            file_path = f"{root}/{filename}"
            load_place(file_path)

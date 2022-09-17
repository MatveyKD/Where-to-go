from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
import json
from places.models import Place, Image
import requests
import os

class Command(BaseCommand):
    help = 'Loading place from json'

    def handle(self, *args, **options):
        if options["load_dir"]:
            load_dir(options["path"])
        else:
            load_place(options["path"])

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--path',
            action='store',
            help='Путь до json файла'
        )
        parser.add_argument(
            '-d',
            '--load_dir',
            action='store_true',
            help='Загрузить все .json файлы из папки'
        )

def load_place(file_path):
    with open(file_path, 'rb') as file:
        content = json.load(file)

    place, _ = Place.objects.get_or_create(
        title = content["title"],
        lng = content["coordinates"]["lng"],
        lat = content["coordinates"]["lat"],
        defaults={
            'description_long': content.get('description_long', ''),
            'description_short': content.get('description_short', ''),
        }
    )

    for index, img in enumerate(content["imgs"]):
        response = requests.get(img)
        Image.objects.get_or_create(
            place = place,
            image = ContentFile(response.content, f"{place.title}{index}.jpg"),
            image_number = index
        )

def load_dir(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            file_path = f"{root}/{filename}"
            load_place(file_path)

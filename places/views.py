from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from places.models import Place
from django.urls import reverse


def index(request):
    places = Place.objects.all()

    context = {
        "places": {
            "type": "FeatureCollection",
            "features": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [place.lng, place.lat]
                    },
                    "properties": {
                        "title": place.title,
                        "placeId": place.id,
                        "detailsUrl": reverse(
                            place_details,
                            kwargs={"place_id": place.id}
                        )
                    }
                }
                for place in places]
        }
    }
    return render(request, "index.html", context)


def place_details(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    place_property = {
        "title": place.title,
        "imgs": [
            image.image.url for image in place.images.all()
        ],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return JsonResponse(
        place_property,
        json_dumps_params={
            "ensure_ascii": False,
            "indent": 4
        },
        safe=False
    )

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import Place, Images


def get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    imgs = Images.objects.filter(title_id=place_id)

    list_imgs = []
    for item in imgs:
        list_imgs.append(item.image.url)

    json_place = {
        "title": place.title,
        "imgs": list_imgs,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat,
        }
    }

    return JsonResponse(json_place,
                        safe=False,
                        json_dumps_params={"ensure_ascii": False, 'indent': 4},
                        )


def home(request):
    places = Place.objects.all()

    features = []
    for item in places:
        features.append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        item.lng,
                        item.lat
                    ]
                },
                "properties": {
                    "title": item.title,
                    "placeId": item.id,
                    "detailsUrl": reverse('place', kwargs={'place_id': item.pk})
                }
            }
        )

    places_geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    context = {
        'places_geojson': places_geojson,
    }
    return render(request, template_name='base.html', context=context)

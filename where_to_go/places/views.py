from django.shortcuts import render
from .models import Place, Images


def home(request):
    places = Place.objects.all()
    imgs = Images.objects.filter()

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
                    "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
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

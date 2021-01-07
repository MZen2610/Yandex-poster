from django.shortcuts import render
from .models import Place, Images
import json


def home(request):
    places = Place.objects.all()
    imgs = Images.objects.filter()

    places_geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        37.62,
                        55.793676
                    ]
                },
                "properties": {
                    "title": "«Легенды Москвы",
                    "placeId": "moscow_legends",
                    "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
                }
            },
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        37.64,
                        55.753676
                    ]
                },
                "properties": {
                    "title": "Крыши24.рф",
                    "placeId": "roofs24",
                    "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/roofs24.json"
                }
            }
        ]
    }

    # print('places_geojson = ', type(places_geojson))

    context = {
        'places_geojson': places_geojson,
        # 'title': 'Hello !!!'
    }
    # return render(request, template_name='places/home.html', context=context)
    return render(request, template_name='base.html', context=context)

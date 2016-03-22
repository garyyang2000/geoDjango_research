__author__ = 'gary'

import os
from django.contrib.gis.utils import LayerMapping
from models import cities

cities_mapping = {
    'name' : 'Name',
    'population' : 'Population',
    'density' : 'Density',
    'created' : 'Created',
    'geom' : 'POINT',
}
cities_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../cities/cities.shp'))

def run(verbose=True):
    lm = LayerMapping(cities, cities_shp, cities_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
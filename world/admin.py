from django.contrib.gis import admin
from models import WorldBorder

class InterestingLocationAdmin(admin.OSMGeoAdmin):
     fieldsets = (
       ('Location Attributes', {'fields': (('name','area','pop2005'))}),
       ('Editable Map View', {'fields': ('mpoly',)}),
     )
     list_display = ('name','area','pop2005')
    # Default GeoDjango OpenLayers map options
     scrollable = False
     map_width = 1000
     map_height = 500

admin.site.register(WorldBorder, InterestingLocationAdmin)

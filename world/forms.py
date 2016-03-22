import floppyforms as forms

class OsmLineStringWidget(forms.gis.BaseOsmWidget,
                          forms.gis.LineStringWidget):
    pass

class GeoForm(forms.Form):
    line = forms.gis.LineStringField(widget=OsmLineStringWidget)
from django import forms

class AccidentForm(forms.Form):
    weather = forms.FloatField(label='Weather Condition')
    road_surface = forms.FloatField(label='Road Surface')
    visibility = forms.FloatField(label='Visibility')
    light_condition = forms.FloatField(label='Light Condition')
from django import forms
import datetime
from django.forms.extras.widgets import SelectDateWidget


class TripForm(forms.Form):
    cityA= forms.CharField(label='From', max_length=100)
    cityB = forms.CharField(label='To', max_length=100)
    day_Of_Travel = forms.DateField(label='Date of Travel', initial=datetime.date.today, widget=SelectDateWidget(empty_label="Nothing"))
    passengers = forms.IntegerField(label='Passenger', min_value=0)


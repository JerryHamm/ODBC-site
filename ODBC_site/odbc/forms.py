from django import forms
from odbc.models import events

class EditEventsForm(forms.ModelForm):
    class Meta:
        model = events
        fields = "__all__"
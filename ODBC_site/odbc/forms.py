from django import forms
from odbc.models import events, work_blog

class EditEventsForm(forms.ModelForm):
    class Meta:
        model = events
        exclude =[ "event_image"]

class AddWorkPost(forms.ModelForm):
    class Meta:
        model = work_blog
        fields = "__all__"

        
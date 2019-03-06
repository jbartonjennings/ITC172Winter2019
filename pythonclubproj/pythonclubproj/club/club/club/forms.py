from django import forms
from .models import Meeting, Resource 

class MeetingForm(forms.Modelform):
    class Meta:
        model=Meeting
        fields='__all__'





class ResourceForm(forms.Modelform):
    class Meta:
        model=Resource
        fields='__all__'
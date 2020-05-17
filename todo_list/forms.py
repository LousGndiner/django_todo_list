from django import forms
from .models import AlumniModel

class ListAlumni(forms.ModelForm):
    class Meta:
        model = AlumniModel
        fields = ['lastName', 'firstName', 'gender', 'year', 'course', 'job', 'employer']

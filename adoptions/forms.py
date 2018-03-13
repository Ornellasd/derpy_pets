from django import forms

from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'submitter', 'species', 'breed', 'description', 'sex', 'age', 'vaccinations']
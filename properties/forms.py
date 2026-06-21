from django import forms
from properties.models import allproperties


class PropertiesForm(forms.ModelForm):

    class Meta:
        model=allproperties
        fields='__all__'

class PropertyEditForm(forms.ModelForm):
    owner_name = forms.CharField(disabled=True)
    class Meta:
        model = allproperties
        fields='__all__'
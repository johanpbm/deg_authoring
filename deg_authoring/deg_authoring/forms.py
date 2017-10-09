'''
Created on 20 set. 2017

@author: jbaldeon
'''
from django import forms
from api.models import DigitalEducationalGameImage

class UploadImageForm(forms.ModelForm):
    
    class Meta:
        model = DigitalEducationalGameImage
        fields = ['digital_educational_game', 'image' ]
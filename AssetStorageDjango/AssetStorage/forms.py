from django import forms
from django.forms import ModelForm

from .models import *


class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ['name', 'file', 'tags', 'related_assets', 'previews']
        help_texts = {

        }

        labels = {
            'name' : 'Asset Name:',
            'file' : 'Upload FBX file:'
        }
        widgets = {
            'name' : forms.TextInput(attrs = {'placeholder' : 'Enter Name of Asset...',
                                              'class' : 'upload-item',
                                              'id' : 'asset-name'}),
            'file' : forms.FileInput(attrs = {'class' : 'upload-item',
                                              'id' : 'main_asset'}),
            #'related_assets' : forms.

        }
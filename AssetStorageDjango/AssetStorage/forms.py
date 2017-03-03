from django import forms
from django.forms import ModelForm, inlineformset_factory

from .models import *
from .helpers.choices import *
#flag for deletion
# class AssetForm(ModelForm):
#     class Meta:
#         model = Asset
#         fields = ['name', 'file', 'tags', 'related_assets', 'previews']
#         help_texts = {
#
#         }
#
#         labels = {
#             'name' : 'Asset Name:',
#             'file' : 'Upload FBX file:'
#         }
#         widgets = {
#             'name' : forms.TextInput(attrs = {'placeholder' : 'Enter Name of Asset...',
#                                               'class' : 'upload-item',
#                                               'id' : 'asset-name'}),
#             'file' : forms.FileInput(attrs = {'class' : 'upload-item',
#                                               'id' : 'main_asset'}),
#             #'related_assets' : forms.
#
#         }

class TagField(forms.TextInput):

    def value_from_datadict(self, data, files, name):
        raw_tags = data.get('tags')
        split_tags = raw_tags.split(',')
        for item in split_tags:
            if Tag.objects.filter(tag=item).exists():
                pass
            else:
                new_tag = Tag.create(item)
                new_tag.save()
        return Tag.objects.filter(tag__in=split_tags)


class SimpleAssetForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SimpleAssetForm, self).__init__(*args, **kwargs)
        self.fields['asset_type'].choices = ASSET_TYPE_CHOICES


    class Meta:
        model = AssetData
        fields = ['name', 'file', 'tags', 'asset_type']

        labels = {
            'name' : 'Asset Name:',
        }

        widgets = {
            'name' : forms.TextInput(attrs = {'placeholder' : 'Enter Name of Asset...',
                                              'class' : 'upload-item',
                                              'id' : 'asset-name'}),
            'file' : forms.FileInput(attrs = {'class' : 'hidden',
                                              'id' : 'main-asset',
                                              }),
            'tags' : TagField(attrs = {'id' : 'asset-tags',
                                       'class' : 'hidden'
                                       }),
            'asset_type' : forms.Select(attrs = { 'id' : 'asset-type'} )

        }

# SimpleAssetFormSet = inlineformset_factory(CompoundAsset, SimpleAsset, form=SimpleAssetForm, extra=3)

# class CompoundAssetForm(ModelForm):
#     class Meta:
#         model = CompoundAsset
#         fields = ['name', 'file', 'tags', 'related_assets']
#
#         labels = {
#             'name' : 'Asset Name:',
#         }
#         widgets = {
#             'name' : forms.TextInput(attrs = {'placeholder' : 'Enter Name of Asset...',
#                                               'class' : 'upload-item',
#                                               'id' : 'asset-name'}),
#             'file' : forms.FileInput(attrs = {'class' : 'hidden',
#                                               'id' : 'main-asset',
#                                               }),
#             'tags' : TagField(attrs = {'id' : 'asset-tags',
#                                        'class' : 'hidden'
#                                       }),
#
#         }










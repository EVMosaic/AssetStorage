from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

import json

from .models import *
from .forms import *

# Create your views here.
class AssetDetailView(DetailView):
    model = Asset
    context_object_name = 'asset'
    template_name = 'AssetStorage/detail_template.html'

    def get_context_data(self, **kwargs):
        context = super(AssetDetailView, self).get_context_data(**kwargs)
        context['kitten'] = 'Goldberry'
        context['main_asset'] = self.get_object().previews.all()[3]
        return context

class UploadView(CreateView):
    model = SimpleAsset
    context_object_name = 'asset'
    template_name = 'ASsetStorage/upload_template.html'
    form_class = SimpleAssetForm

    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        tag_list = []
        for t in tags:
            tag_list.append(t.tag)
        json_tags = json.dumps(tag_list)
        context['tags'] = json_tags
        print(json_tags)
        print(context)
        return context
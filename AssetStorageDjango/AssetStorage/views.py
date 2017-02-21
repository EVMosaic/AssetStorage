from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.core import serializers

from django.db.models import Count
from django.http import JsonResponse


from django.shortcuts import redirect

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
        context['main_asset'] = self.get_object().previews.all()[3]
        return context

class SimpleAssetView(DetailView):
    model = SimpleAsset
    context_object_name = 'asset'
    template_name = 'AssetStorage/simple_detail_template.html'

    def get_context_data(self, **kwargs):
        context = super(SimpleAssetView, self).get_context_data(**kwargs)
        context['tags'] = self.get_object().tags.all().order_by('tag')
        print(context['tags'])
        return context

class UploadView(CreateView):
    model = SimpleAsset
    context_object_name = 'asset'
    template_name = 'AssetStorage/upload_template.html'
    form_class = SimpleAssetForm
    success_url = '/upload'

    def get_context_data(self, **kwargs):
        context = super(UploadView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        tag_list = []
        for t in tags:
            tag_list.append(t.tag)
        json_tags = json.dumps(tag_list)
        context['tags'] = json_tags
        return context

    def get_success_url(self):
        print('id:')
        return reverse('simple-detail', args=(self.object.pk,))


class SearchView(ListView):
    model = SimpleAsset
    template_name = 'AssetStorage/search_template.html'
    context_object_name = 'assets'

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        print('getting context data')
        # print(str(context['assets'].count()) + ' assets with files')
        context['assets'] = SimpleAsset.objects.exclude(file='').order_by('name')
        # print(str(context['assets'].count()) + ' assets without files')
        context['tags'] = Tag.objects.annotate(asset_count=Count('simple_assets'))\
                          .filter(asset_count__gt=0).order_by('-asset_count', 'tag')
        return context

    def post(self, request, *args, **kwargs):
        print("posting!")
        print(request.POST['tag-list'])
        tag = request.POST['tag-list']
        selected_tag = Tag.objects.get(pk=tag)
        related_assets = selected_tag.simple_assets.all().order_by('name')
        print(Tag.objects.get(pk=request.POST['tag-list']).simple_assets.all())
        data = []
        print(data)
        for asset in related_assets:
            print(asset)
            object_dict = {
                'pk': asset.pk,
                'thumb': asset.thumb.url,
                'name': asset.name,
                'file': asset.file.path,
                'size': asset.pretty_file_size()
            }
            data.append(object_dict)
        # data = serializers.serialize('json', related_assets)
        return JsonResponse(json.dumps(data), safe=False)


def searchAPI(request, *args, **kwargs):
    print('entering search api')
    print(args)
    print(kwargs)
    print(request)
    print(request.POST)
    return JsonResponse({'kitten' : 'goldberry'})

# class searchAPI(FormView):
#     pass
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
        # print(str(context['assets'].count()) + ' assets with files')
        context['assets'] = SimpleAsset.objects.exclude(file='').order_by('name')
        # print(str(context['assets'].count()) + ' assets without files')
        context['tags'] = Tag.objects.annotate(asset_count=Count('simple_assets'))\
                          .filter(asset_count__gt=0).order_by('-asset_count', 'tag')
        return context

    def post(self, request, *args, **kwargs):
        # should probably move this all into an ajax check and extract into own function
        # for item in request.environ:
        #     print(str(item) + ":" + str(request.environ[item]));
        # print(request.body)
        if request.is_ajax():
            print("found an ajax request")
        # return self.filter_tags(request)
        return self.search_by_name(request)

    def search_by_name(self, request):
        search_query = request.POST['search-box']
        print('searching for: ' + search_query)
        search_results = SimpleAsset.objects.filter(name__icontains=search_query)
        print(search_results)
        data = self.queryset_to_jquery(search_results)

        return JsonResponse(data, safe=False)

    def filter_tags(self, request):
        requested_tags = list(filter(None, request.POST['selected-tags'].split(':')))
        related_assets = SimpleAsset.objects.filter(tags__pk__in=requested_tags) \
            .annotate(num_tags=Count('tags')) \
            .filter(num_tags=len(requested_tags)) \
            .order_by('name')
        # ^ this does some magic that i cant completely understand but it seems to work...
        # it seems to be counting the number of matches, but i dont understand why
        # the Count('tags') isnt counting the number of tags on the model
        # regardless this is used to filter on ALL tags in a list instead of ANY
        data = self.queryset_to_jquery(related_assets)
        return JsonResponse(data, safe=False)

    def queryset_to_jquery(self, queryset):
        if len(queryset) == 0:
            return json.dumps({})
        tagged_assets = []
        related_tags = []
        for asset in queryset:
            tags = asset.tags.all()
            for item in tags:
                related_tags.append(item.pk)
            object_dict = {
                'pk': asset.pk,
                'thumb': asset.thumb.url,
                'name': asset.name,
                'file': asset.file.path,
                'size': asset.pretty_file_size()
            }
            tagged_assets.append(object_dict)
        data = {
            'assets': tagged_assets,
            'tags': list(set(related_tags))
        }
        return json.dumps(data)

from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import *

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
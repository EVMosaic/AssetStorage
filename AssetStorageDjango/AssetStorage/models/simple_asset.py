from django.db import models
from .compound_asset import CompoundAsset

class SimpleAsset(models.Model):
    name = models.CharField(max_length=200)
    models_using = models.ManyToManyField(CompoundAsset, blank=True, related_name='simple_assets')
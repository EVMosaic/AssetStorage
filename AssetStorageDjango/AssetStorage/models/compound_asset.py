from django.db import models

class CompoundAsset(models.Model):
    name = models.CharField(max_length=200)
    models_using = models.ManyToManyField('self', blank=True, related_name='simple_assets')
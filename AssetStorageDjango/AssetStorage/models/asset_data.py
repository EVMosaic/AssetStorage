from django.db import models

from .simple_asset import SimpleAsset
from .tag import Tag
from ..helpers .utilities import make_thumbnail, convert_size
from ..helpers.choices import *


class AssetData(models.Model):
    upload_folder = "test_folder"
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to=upload_folder, blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    #change related name and check other classes after rename
    tags = models.ManyToManyField(Tag, related_name="simple_assets", blank=True)
    thumb = models.ImageField(upload_to=upload_folder, blank=True)
    asset = models.ForeignKey(SimpleAsset, blank=True)
    asset_type = models.CharField(max_length=200, choices=ASSET_TYPE_CHOICES )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Simple Asset"

    def pretty_file_size(self):
        return convert_size(self.file.size)

    def save(self, *args, **kwargs):
        super(AssetData, self).save(*args, **kwargs)
        if not self.thumb:
            self.thumb = make_thumbnail(self.file , 75, 75)
            super(AssetData, self).save(*args, **kwargs)
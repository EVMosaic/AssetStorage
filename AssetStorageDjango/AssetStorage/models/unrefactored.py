from django.db import models
from .utilities import convert_size
from .asset_data import AssetData
from .tag import Tag

class CompoundAsset(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to="test_folder", blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="compound_assets", blank=True)
    related_assets = models.ManyToManyField(AssetData, related_name="parents")
    hero = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Compound Asset"

    def pretty_file_size(self):
        return convert_size(self.file.size)


class Texture(models.Model):
    name = models.CharField(max_length=200)
    date_uploaded = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="compound_assets", blank=True)
    # texture_files = models.ManyToManyField(SimpleAsset, related_name='texture', through=)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Texture Asset"


class PreviewImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="test/previews")
    thumb = models.ImageField(upload_to="test/thumbs")
    mainAsset = models.ForeignKey(CompoundAsset, related_name="previews")

    def __str__(self):
        return self.name

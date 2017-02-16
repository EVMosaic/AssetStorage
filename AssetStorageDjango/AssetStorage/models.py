import os
from django.db import models
from django.core.files import File
from AssetStorage import utilities


# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    @classmethod
    def create(cls, tag):
        new_tag = Tag(tag=tag)
        return new_tag

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Tag"


class PreviewImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="test/previews")
    thumb = models.ImageField(upload_to="test/thumbs")

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to="test_folder", blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="assets", blank=True)
    related_assets = models.ManyToManyField('self', through="RelatedAssets", symmetrical=False)
    previews = models.ManyToManyField(PreviewImage, related_name="preview", blank=True)

    def __str__(self):
        return self.name

    def pretty_file_size(self):
        return utilities.convert_size(self.file.size)

    def main_preview(self):
        try:
            return self.previews.all()[0].thumb.url
        except:
            return ""

    def support_preview(self):
        return self.supporting_asset.previews.all()[0].thumb.url

    class Meta:
        verbose_name = "Asset"

class SimpleAsset(models.Model):
    upload_folder = "test_folder"
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to=upload_folder, blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="simple_assets", blank=True)
    thumb = models.ImageField(upload_to=upload_folder, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Simple Asset"

    def pretty_file_size(self):
        return utilities.convert_size(self.file.size)

    def save(self, *args, **kwargs):
        super(SimpleAsset, self).save(*args, **kwargs)
        if not self.thumb:
            self.thumb = utilities.make_thumbnail(self.file , 75, 75)
            super(SimpleAsset, self).save(*args, **kwargs)




class CompoundAsset(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to="test_folder", blank=True, null=True)
    date_uploaded = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="compound_assets", blank=True)
    related_assets = models.ManyToManyField(SimpleAsset, related_name="parents")
    previews = models.ManyToManyField(PreviewImage, related_name="compound_assets", blank=True)
    hero = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Compound Asset"

    def __str__(self):
        return self.name

    def pretty_file_size(self):
        return utilities.convert_size(self.file.size)





class RelatedAssets(models.Model):
    main_asset = models.ForeignKey(Asset, related_name="main_asset")
    supporting_asset = models.ForeignKey(Asset, related_name="supporting_asset")

    def support_preview(self):
        return self.supporting_asset.previews.all()[0].thumb.url

    class Meta:
        verbose_name = "Asset"




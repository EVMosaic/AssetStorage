from django.db import models

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=100)
    # assets = models.ManyToManyField(Asset, through=Asset.tags.through, blank=True)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = "Tag"


class Asset(models.Model):
    name = models.CharField(max_length=200)
    path = models.CharField(max_length=300)
    file_size = models.FloatField()
    date_uploaded = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag, related_name="assets", blank=True)
    related_assets = models.ManyToManyField('self', through="RelatedAssets", symmetrical=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Asset"


class RelatedAssets(models.Model):
    main_asset = models.ForeignKey(Asset, related_name="main_asset")
    supporting_asset = models.ForeignKey(Asset, related_name="supporting_asset")

    class Meta:
        verbose_name = "Asset"
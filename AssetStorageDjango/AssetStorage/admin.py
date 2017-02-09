from django.contrib import admin
from .models import *

# Register your models here.

class RelatedAssetsInline(admin.TabularInline):
    model = RelatedAssets
    extra = 1
    fk_name = "main_asset"

class MainAssetsInline(admin.TabularInline):
    model = RelatedAssets
    extra = 0
    fk_name = "supporting_asset"

class TaggedAssetsInline(admin.TabularInline):
    model = Asset.tags.through
    extra = 0
    # fk_name = "assets"

class AssetAdmin(admin.ModelAdmin):
    inlines = [RelatedAssetsInline, MainAssetsInline]


class TagAdmin(admin.ModelAdmin):
    inlines = [TaggedAssetsInline]
    fields = ['tag']


admin.site.register(Asset, AssetAdmin)
admin.site.register(Tag, TagAdmin)

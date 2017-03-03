# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 19:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AssetStorage', '0008_auto_20170215_1438'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SimpleAsset',
            new_name='AssetData',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='previews',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='related_assets',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='compoundasset',
            name='previews',
        ),
        migrations.RemoveField(
            model_name='compoundasset',
            name='related_assets',
        ),
        migrations.RemoveField(
            model_name='compoundasset',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='relatedassets',
            name='main_asset',
        ),
        migrations.RemoveField(
            model_name='relatedassets',
            name='supporting_asset',
        ),
        migrations.DeleteModel(
            name='Asset',
        ),
        migrations.DeleteModel(
            name='CompoundAsset',
        ),
        migrations.DeleteModel(
            name='PreviewImage',
        ),
        migrations.DeleteModel(
            name='RelatedAssets',
        ),
    ]

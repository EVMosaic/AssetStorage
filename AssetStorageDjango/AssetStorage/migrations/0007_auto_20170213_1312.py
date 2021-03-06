# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetStorage', '0006_auto_20170212_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompoundAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(blank=True, null=True, upload_to='test_folder')),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('hero', models.IntegerField(default=0)),
                ('previews', models.ManyToManyField(blank=True, related_name='compound_assets', to='AssetStorage.PreviewImage')),
            ],
            options={
                'verbose_name': 'Compound Asset',
            },
        ),
        migrations.CreateModel(
            name='SimpleAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('file', models.FileField(blank=True, null=True, upload_to='test_folder')),
                ('date_uploaded', models.DateField(auto_now_add=True)),
                ('date_updated', models.DateField(auto_now=True)),
                ('thumb', models.ImageField(upload_to='test/thumbs')),
                ('tags', models.ManyToManyField(blank=True, related_name='simple_assets', to='AssetStorage.Tag')),
            ],
            options={
                'verbose_name': 'Simple Asset',
            },
        ),
        migrations.AddField(
            model_name='compoundasset',
            name='related_assets',
            field=models.ManyToManyField(related_name='parents', to='AssetStorage.SimpleAsset'),
        ),
        migrations.AddField(
            model_name='compoundasset',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='compound_assets', to='AssetStorage.Tag'),
        ),
    ]

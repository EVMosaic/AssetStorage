from django.db import models
from .utilities import make_thumbnail, convert_size
from .tag import Tag
from .simple_asset import SimpleAsset

ASSET_TYPE_CHOICES = (
    ('Texture', (
            ('diffuse', 'Diffuse Map'),
            ('normal', 'Normal Map'),
            ('bump', 'Bump Map'),
            ('displacement', 'Displacement Map'),
            ('alpha', 'Alpha Map'),
            ('ao', 'Detail Map'),
            ('specular', 'Specular Map'),
            ('rough', 'Roughness Map'),
            ('gloss', 'Glossiness Map'),
            ('metal', 'Metalness Map'),
            ('emission', 'Emission Map'),
            ('environment', 'Environment Map'),
            ('texture', 'Other Texture Map')
        )
    ),
    ('3D', (
            ('model', '3D Model'),
            ('material', '3D Material'),
            ('unity', 'Unity Asset Bundle'),
            ('blend', 'Blender File'),
            ('maya', 'Maya File'),
            ('max', '3DS Max File'),
            ('sketch', 'Sketchup File'),
            ('3d', 'Other 3D File')
        )
    ),
    ('Audio', (
            ('voiceover', 'Voiceover'),
            ('sfx', 'Sound Effects'),
            ('music', 'Music'),
            ('audio', 'Other Audio File')
        )
    ),
    ('Video', (
            ('animatic', 'Animatic'),
            ('final', 'Final Video'),
            ('video', 'Other Video File')
        )
    ),
    ('Image', (
            ('logo', 'Logo'),
            ('icon', 'Icon'),
            ('raster', 'Raster Image'),
            ('vector', 'Vector'),
            ('cutout', 'Cutout'),
            ('photo', 'Photo'),
            ('background', 'Background Image'),
            ('texture', 'Texture Image'),
            ('image', 'Other Image File')
        )
    ),
    ('Code', (
            ('csharp', 'C#'),
            ('html', 'HTML'),
            ('css', 'CSS'),
            ('sass', 'SASS'),
            ('js', 'Javascript'),
            ('php', 'Php'),
            ('python', 'Python'),
            ('xml', 'XML'),
            ('code', 'Other Programming Language')
        )
    ),
    ('other', 'Other')
)


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
    asset_type = models.CharField(max_length=200, choices=ASSET_TYPE_CHOICES)

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
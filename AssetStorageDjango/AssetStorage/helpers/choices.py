
CODE_TYPES = (
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


IMAGE_TYPES = (
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

VIDEO_TYPES = (
    ('animatic', 'Animatic'),
    ('final', 'Final Video'),
    ('video', 'Other Video File')
)

AUDIO_TYPES = (
    ('voiceover', 'Voiceover'),
    ('sfx', 'Sound Effects'),
    ('music', 'Music'),
    ('audio', 'Other Audio File')
)

THREE_D_TYPES = (
    ('model', '3D Model'),
    ('material', '3D Material'),
    ('unity', 'Unity Asset Bundle'),
    ('blend', 'Blender File'),
    ('maya', 'Maya File'),
    ('max', '3DS Max File'),
    ('sketch', 'Sketchup File'),
    ('3d', 'Other 3D File')
)

TEXTURE_TYPES = (
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

ASSET_TYPE_CHOICES = (
   ('Textures', TEXTURE_TYPES),
   ('3D', THREE_D_TYPES),
   ('Audio', AUDIO_TYPES),
   ('Video', VIDEO_TYPES),
   ('Images', IMAGE_TYPES),
   ('Progamming Language', CODE_TYPES),
   ('other', 'Other'),
)
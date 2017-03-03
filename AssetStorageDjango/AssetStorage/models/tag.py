from django.db import models

# TODO add field to count references/update on save (# of tags/# of assets using)
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

import uuid

from djongo import models

from django.db.models.signals import post_save
from django.dispatch import receiver


# + ------------------------------------------------------------------------- +
def get_upload_video_path(instance: object, filename: str) -> str:
    """ returns a dinamic path to sabe each video file """
    path = "videos/{}/file/{}".format(instance.id, filename)

    return path
# + ------------------------------------------------------------------------- +


# Models


# + ------------------------------------------------------------------------- +
class Theme(models.Model):
    """ Theme Document """
    id = models.UUIDField(primary_key=True, editable=False,
                          unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=30)
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)
    score = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        self.score = self.thumbs_up - (self.thumbs_down / 2)
        super(Theme, self).save(*args, **kwargs)

    def __str__(self: object) -> str:
        return self.name
# + ------------------------------------------------------------------------- +


# + ------------------------------------------------------------------------- +
class Video(models.Model):
    id = models.UUIDField(primary_key=True, editable=False,
                          unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=200)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    file = models.FileField(upload_to=get_upload_video_path)
    thumbs_up = models.IntegerField(default=0)
    thumbs_down = models.IntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# + ------------------------------------------------------------------------- +


# Signals


# + ------------------------------------------------------------------------- +
@receiver(post_save, sender=Video)
def like_and_unlike(sender, instance, created, **kwargs):
    if not created:
        thumbs_up = 0
        thumbs_down = 0

        videos_with_this_theme = Video.objects.filter(theme__id=instance.theme.id)
        for video in videos_with_this_theme:
            thumbs_up += video.thumbs_up
            thumbs_down += video.thumbs_down
        
        theme = Theme.objects.filter(id=instance.theme.id).first()
        theme.thumbs_up = thumbs_up
        theme.thumbs_down = thumbs_down
        theme.save()

        print("pronto!")
# + ------------------------------------------------------------------------- +

import uuid
from djongo import models


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

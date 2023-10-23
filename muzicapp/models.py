from django.db import models


class Muzic(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    url = models.TextField()
    img_url = models.URLField()
    def __str__(self):
        return self.title
        

        


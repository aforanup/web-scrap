from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField()
    author = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    read_time = models.IntegerField()

    def __str__(self):
        return f"{self.author} {self.title}"

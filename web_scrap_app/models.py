from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author_image = models.URLField()
    blog_image = models.URLField()
    author_name = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    read_time = models.CharField(max_length=35)

    def __str__(self):
        return f"{self.author_name} {self.title}"

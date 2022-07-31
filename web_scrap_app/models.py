from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    author_image = models.URLField(null=True)
    blog_image = models.URLField(null=True)
    author_name = models.CharField(max_length=255, null=True)
    author_designation = models.CharField(max_length=255, null=True)
    read_time = models.CharField(max_length=35, null=True)

    def __str__(self):
        return f"{self.author_name} {self.title}"

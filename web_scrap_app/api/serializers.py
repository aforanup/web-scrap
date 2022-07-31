from rest_framework import serializers
from .. import models


class BlogViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = "__all__"

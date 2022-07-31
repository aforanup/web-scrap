import os

from django.core.management.base import BaseCommand, CommandError
from web_scrap_app.models import Blog
import json
from django.conf import settings

path = os.path.join(
    settings.BASE_DIR, "web_scrap_app/management/commands/scrapped_data.json"
)

with open(path, "r") as f:
    blogs = json.loads(f.read())


class Command(BaseCommand):
    help = "Initialize database with default blogs"

    def handle(self, *args, **options):
        for i in range(int(12000 / len(blogs))):
            for blog in blogs:
                try:
                    Blog.objects.create(
                        title=blog.get("title"),
                        read_time=blog.get("read_time"),
                        description=blog.get("description"),
                        author_image=blog.get("author_image"),
                        author_name=blog.get("author_name"),
                        author_designation=blog.get("author_designation"),
                        blog_image=blog.get("blog_image"),
                    )
                    print(f"{i}: {blog.get('title')} data created.")
                except:
                    print("Couldn't create blog")
                    pass

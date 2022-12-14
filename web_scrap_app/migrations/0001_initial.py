# Generated by Django 3.2.14 on 2022-07-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('author_image', models.URLField()),
                ('blog_image', models.URLField()),
                ('author_name', models.CharField(max_length=255)),
                ('author_designation', models.CharField(max_length=255)),
                ('read_time', models.CharField(max_length=35)),
            ],
        ),
    ]

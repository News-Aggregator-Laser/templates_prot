# Generated by Django 4.1.3 on 2023-01-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="New",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("sub_title", models.CharField(max_length=350)),
                ("content", models.TextField()),
                ("category", models.CharField(max_length=100)),
                ("image_url", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=100)),
                ("provider", models.CharField(max_length=100)),
                ("published_at", models.DateTimeField()),
            ],
        ),
    ]

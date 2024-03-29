# Generated by Django 4.1.9 on 2024-02-02 22:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="atchviements",
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
                ("img", models.CharField(max_length=50)),
                ("topic", models.CharField(max_length=50)),
                ("date_place", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="certificate",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("img", models.CharField(max_length=50)),
                ("topic", models.CharField(max_length=50)),
                ("date_place", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="hackthons",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("img", models.CharField(max_length=50)),
                ("topic", models.CharField(max_length=50)),
                ("sub_topic", models.CharField(max_length=50)),
                ("date_place", models.CharField(max_length=50)),
                ("team", models.CharField(max_length=50)),
                ("result", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="profile_pic",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("img", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="projects",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("img", models.CharField(max_length=500)),
                ("topic", models.CharField(max_length=500)),
                ("date_place", models.CharField(max_length=500)),
                ("paragraph", models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name="resume",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("img", models.CharField(max_length=50)),
                ("last_date", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Roles",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("img", models.CharField(max_length=50)),
                ("company", models.CharField(max_length=50)),
                ("discrption", models.CharField(max_length=50)),
                ("link", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="skill",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("language", models.CharField(max_length=50)),
                ("persentage", models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 4.1.7 on 2023-04-24 13:11

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import wagtail.models.collections
import wagtail.search.index


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0083_workflowcontenttype"),
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomDocument",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="title")),
                ("file", models.FileField(upload_to="documents", verbose_name="file")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                ("file_size", models.PositiveIntegerField(editable=False, null=True)),
                (
                    "file_hash",
                    models.CharField(blank=True, editable=False, max_length=40),
                ),
                (
                    "collection",
                    models.ForeignKey(
                        default=wagtail.models.collections.get_root_collection_id,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="wagtailcore.collection",
                        verbose_name="collection",
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text=None,
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="tags",
                    ),
                ),
            ],
            options={
                "verbose_name": "document",
                "verbose_name_plural": "documents",
                "abstract": False,
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
    ]

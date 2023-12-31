# Generated by Django 4.2 on 2023-05-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_alter_entry_authors"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="entry",
            name="authors",
            field=models.ManyToManyField(related_name="entries", to="posts.author"),
        ),
    ]

# Generated by Django 5.2.2 on 2025-06-15 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("twitterapp1", "0010_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="postsfiles/"),
        ),
    ]

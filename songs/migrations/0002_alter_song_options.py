# Generated by Django 4.2 on 2023-04-18 20:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("songs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="song",
            options={"ordering": ("id",)},
        ),
    ]

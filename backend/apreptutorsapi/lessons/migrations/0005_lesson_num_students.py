# Generated by Django 4.1.9 on 2023-07-04 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lessons", "0004_lesson_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="num_students",
            field=models.IntegerField(default=1),
        ),
    ]

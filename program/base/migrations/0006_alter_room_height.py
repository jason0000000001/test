# Generated by Django 3.2.7 on 2022-11-05 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_room_image_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='height',
            field=models.IntegerField(default=True),
        ),
    ]

# Generated by Django 3.2.7 on 2022-10-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20221024_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='height',
            field=models.FloatField(default=True),
        ),
        migrations.AddField(
            model_name='room',
            name='image_id',
            field=models.CharField(default=True, max_length=45),
        ),
    ]

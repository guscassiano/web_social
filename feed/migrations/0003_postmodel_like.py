# Generated by Django 5.0.7 on 2024-09-05 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_remove_postmodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='like',
            field=models.BooleanField(blank=True, default=False, verbose_name='Curtida'),
            preserve_default=False,
        ),
    ]

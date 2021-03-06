# Generated by Django 2.2.19 on 2021-04-01 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('behavior', '0007_auto_20210401_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='originator',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='originators', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

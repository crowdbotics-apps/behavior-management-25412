# Generated by Django 2.2.19 on 2021-04-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('behavior', '0005_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='name',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.2.19 on 2021-04-01 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('behavior', '0004_auto_20210401_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
    ]

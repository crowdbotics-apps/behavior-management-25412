from django.conf import settings
from django.db import models


class Behavior(models.Model):
    "Generated Model"
    date = models.DateTimeField()
    trigger = models.CharField(
        max_length=256,
    )
    intensity = models.PositiveSmallIntegerField()
    consequence = models.CharField(
        max_length=256,
    )
    originator = models.ForeignKey(
        "behavior.Originator",
        on_delete=models.PROTECT,
        related_name="behavior_originator",
    )


class Originator(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=255,
    )
    age = models.PositiveIntegerField(
        max_length=50,
    )
    sex = models.CharField(
        max_length=256,
    )


# Create your models here.

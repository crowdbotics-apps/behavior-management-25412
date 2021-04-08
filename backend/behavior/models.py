# Create your models here.

from django.db import models
from django.utils.translation import ugettext_lazy as _

from home.models import OwnedModel


class Behavior(OwnedModel):
    date = models.DateTimeField()
    trigger = models.CharField(
        _("Gatilho"),
        max_length=256,
    )
    behavior = models.CharField(
        _("Comportamento"),
        max_length=255
    )
    additional_info = models.TextField(
        _("Informações adicionais"),
        blank=True, null=True, default=""
    )
    intensity = models.PositiveSmallIntegerField(_("Intensidade (0/100)"))
    consequence = models.CharField(
        _("Consequência"),
        max_length=256,
    )
    originator = models.ForeignKey(
        "behavior.Originator",
        verbose_name=_("Causador"),
        on_delete=models.PROTECT,
        related_name="behavior_originator",
    )

    class Meta:
        verbose_name = _("Comportamento")
        verbose_name_plural = _("Comportamentos")

    def __str__(self):
        return f"{self.originator.name}, {self.date.date()}"


class Originator(OwnedModel):
    owner = models.ForeignKey(
        'users.User', related_name="originators", on_delete=models.PROTECT,
        verbose_name=_("Responsável"),
    )
    name = models.CharField(
        verbose_name=_("Nome"),
        max_length=255,
    )
    age = models.PositiveIntegerField(verbose_name=_("Idade"))
    sex = models.CharField(
        verbose_name=_("Sexo"),
        max_length=256,
    )

    class Meta:
        verbose_name = _("Originador")
        verbose_name_plural = _("Originadores")

    def __str__(self):
        return self.name


class Week(OwnedModel):
    owner = models.ForeignKey(
        'users.User', related_name="weeks", on_delete=models.PROTECT
    )
    name = models.CharField(verbose_name=_("Nome"), max_length=255)
    start_date = models.DateField(verbose_name=_("Data inicio"),)
    end_date = models.DateField(verbose_name=_("Data fim"),)

    class Meta:
        ordering = ["id"]
        verbose_name = _("Semana")
        verbose_name_plural = _("Semanas")

    def __str__(self):
        return f"{self.start_date} to {self.end_date}"

# Django Libraries
# Standard Libraries
import os

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Thirdparty Libraries
from ckeditor.fields import RichTextField
from simple_history.models import HistoricalRecords


# #################################################################################### #
class PrecioLote(models.Model):
    history = HistoricalRecords()
    dominio = models.ForeignKey(
        "dominio.Dominio",
        verbose_name=_("Domain"),
        on_delete=models.PROTECT,
        db_index=True,
        related_name="lote_precio_dominios",
        blank=True,
        null=True,
    )
    fecha_publicacion = models.DateTimeField(
        verbose_name=_("Lot Price Publication Date"), auto_now_add=True
    )
    archvo = models.FileField(
        verbose_name=_("Lot Price File"),
        max_length=255,
        upload_to="precio/default.ods",
        blank=True,
        null=True,
    )

    def __str__(self):
        return "{} {}".format(self.dominio, self.fecha_publicacion)

    class Meta:
        ordering = ["dominio", "fecha_publicacion"]
        verbose_name = _("Lot Price")
        verbose_name_plural = _("Lot Price")


# #################################################################################### #
class PrecioDivisa(models.Model):
    USD = "USD"
    COIN_CHOICES = [
        (USD, "USD"),
    ]
    history = HistoricalRecords()
    coin = models.CharField(max_length=2, choices=COIN_CHOICES, default=USD,)
    fecha_publicacion = models.DateTimeField(
        verbose_name=_("Coin price publication date"), auto_now_add=True
    )
    monto = models.IntegerField(verbose_name=_("Amount"))

    def __str__(self):
        return "{} {}".format(self.lote.dominio, self.producto.nombre)

    class Meta:
        ordering = ["coin", "fecha_publicacion"]
        verbose_name = _("Detailed Price")
        verbose_name_plural = _("Detailed Prices")


# #################################################################################### #
class PrecioDetalle(models.Model):
    history = HistoricalRecords()
    lote = models.ForeignKey(
        "PrecioLote",
        verbose_name=_("Lot Price"),
        on_delete=models.PROTECT,
        db_index=True,
        related_name="detalle_precio_lotes",
        blank=True,
        null=True,
    )
    producto = models.ForeignKey(
        "Producto",
        verbose_name=_("Product"),
        on_delete=models.PROTECT,
        db_index=True,
        related_name="detalle_precio_productos",
        blank=True,
        null=True,
    )
    monto = models.IntegerField(verbose_name=_("Amount"))

    def __str__(self):
        return "{} {}".format(self.lote.dominio, self.producto.nombre)

    class Meta:
        ordering = ["lote__dominio", "producto__nombre"]
        verbose_name = _("Detailed Price")
        verbose_name_plural = _("Detailed Prices")

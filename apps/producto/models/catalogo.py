# Django Libraries
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Thirdparty Libraries
from ckeditor.fields import RichTextField
from helpers import SobreEscribirArchivo
from simple_history.models import HistoricalRecords


# class status_catalogo(models.Model):
#     descripcion = models.CharField(max_length=50)
#     fecha_fin = models.DateField(default=timezone.now)
#     status = models.BooleanField(default=True)


# class tipo_producto(models.Model):
#     descripcion = models.CharField(max_length=50)
#     fecha_inicio = models.DateField(null=True, editable=True)
#     status = models.BooleanField(default=True)


# class tipo_moneda(models.Model):
#     descripcion = models.CharField(max_length=50)
#     fecha_inicio = models.DateField(null=True, editable=True)
#     status = models.BooleanField(default=True)


class Categoria(models.Model):
    history = HistoricalRecords()
    nombre = models.CharField(verbose_name=_("Product Name"), max_length=256)
    descripcion = RichTextField(
        verbose_name=_("Product Description"), blank=True, null=True
    )
    fecha = models.DateField(default=timezone.now)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        ordering = ["nombre"]
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


# class catalogo(models.Model):
#     producto = models.CharField(max_length=50)
#     descripcion = models.CharField(max_length=50)
#     categoria = models.ForeignKey(
#         "Categoria", null=True, blank=True, on_delete=models.CASCADE
#     )
#     fecha_inicio = models.DateField(default=timezone.now)
#     status = models.ForeignKey(
#         status_catalogo, null=True, blank=True, on_delete=models.CASCADE
#     )
#     img_url = models.FileField(upload_to="myfolder/", blank=True, null=True)


# class precio(models.Model):
#     producto = models.ForeignKey(
#         "Categoria", null=True, blank=True, on_delete=models.CASCADE
#     )
#     tipo_moneda = models.ForeignKey(
#         tipo_moneda, null=True, blank=True, on_delete=models.CASCADE
#     )
#     precio = models.DecimalField(max_digits=50, decimal_places=3, default="")
#     fecha_inicio = models.DateField(default=timezone.now)
#     fecha_mod = models.DateField(null=True, editable=True)
#     fecha_mod = models.DateField(null=True, editable=True)


# class cantidad(models.Model):
#     producto = models.ForeignKey(
#         "Categoria", null=True, blank=True, on_delete=models.CASCADE
#     )
#     tipo_producto = producto = models.ForeignKey(
#         tipo_producto, null=True, blank=True, on_delete=models.CASCADE
#     )
#     cantidad = models.DecimalField(max_digits=50, decimal_places=3, default="")
#     fecha_inicio = models.DateField(default=timezone.now)
#     fecha_mod = models.DateField(null=True, editable=True)
#     fecha_mod = models.DateField(null=True, editable=True)

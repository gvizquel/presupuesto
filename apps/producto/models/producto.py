# Django Libraries
# Standard Libraries
import os

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Thirdparty Libraries
from ckeditor.fields import RichTextField
from helpers import SobreEscribirArchivo
from simple_history.models import HistoricalRecords


def image_path_producto(instance, filename):
    """Ruta para almacenar las imagenes de los productos
    """
    return os.path.join("producto", str(instance.pk) + "." + filename.rsplit(".", 1)[1])


# #################################################################################### #
class Producto(models.Model):
    NACIONAL = "NACIONAL"
    IMPORTADO = "IMPORTADO"
    PRODUCT_ORGIN_CHOICES = [
        (NACIONAL, "NACIONAL"),
        (IMPORTADO, "IMPORTADO"),
    ]
    history = HistoricalRecords()
    dominio = models.ForeignKey(
        "dominio.Dominio",
        on_delete=models.PROTECT,
        db_index=True,
        related_name="producto_dominios",
        blank=True,
        null=True,
        verbose_name=_("Product Domain"),
    )
    codigo = models.CharField(verbose_name=_("Product Code"), max_length=256)
    codigo_barra = models.CharField(verbose_name=_("Product Bar Code"), max_length=256)
    nombre = models.CharField(verbose_name=_("Product Name"), max_length=256)
    descripcion = RichTextField(
        verbose_name=_("Product Description"), blank=True, null=True
    )
    categoria = models.ManyToManyField(
        "Categoria",
        verbose_name=_("Product Category"),
        related_name="categorias",
        blank=True,
    )
    origen = models.CharField(
        max_length=2, choices=PRODUCT_ORGIN_CHOICES, default=NACIONAL,
    )
    fecha_publicacion = models.DateField(
        verbose_name=_("Product Publication Date"), auto_now_add=True
    )
    imagen = models.ImageField(
        verbose_name=_("Product Image"),
        max_length=255,
        null=True,
        default="product/default.png",
        storage=SobreEscribirArchivo(),
        upload_to=image_path_producto,
        blank=True,
    )

    def __str__(self):
        return "{}".format(self.nombre)

    class Meta:
        ordering = ["dominio", "nombre"]
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

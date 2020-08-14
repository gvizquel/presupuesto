# Django Libraries
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Thirdparty Libraries
from ckeditor.fields import RichTextField

# Own Libraries
from main.models import MainModel


# #################################################################################### #
class Dominio(MainModel):
    nombre = models.CharField(verbose_name=_("Domain Name"), max_length=256)
    razon_social = models.CharField(
        verbose_name=_("Domain Business name"), max_length=256
    )

    def __str__(self):
        return "{}".format(self.razon_social)

    class Meta:
        ordering = ["razon_social"]
        verbose_name = _("Domain")
        verbose_name_plural = _("Domains")

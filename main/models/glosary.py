# -*- coding: utf-8
"""
Modelo de datos de la app main
"""
# Future Libraries
# Librerias Future
from __future__ import unicode_literals

# Django Libraries
from django.db import models

# Thirdparty Libraries
from ckeditor.fields import RichTextField

# Local Folders Libraries
from .main import MainModel


# ========================================================================== #
class Glosary(MainModel):
    """
    Modelo administrativo: Almacena la definición de los terminos utilizados en
    FincaSoft
    """
    termino = models.CharField(max_length=255)
    resumen = models.CharField(max_length=255)
    definicion = RichTextField()

    def __str__(self):
        return self.termino

    class Meta:
        verbose_name = "Término"
        verbose_name_plural = "Glosary de términos"

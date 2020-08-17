# Standard Libraries
import logging
import uuid
from datetime import date, datetime, timedelta
from io import BytesIO
from multiprocessing.pool import ThreadPool

# Django Libraries
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail
from django.utils.translation import ugettext as _

# Thirdparty Libraries
from aitrade_core.models import Country
from aitrade_core.tasks import SednMailCelery
from aitrade_logging.models import TransactionFileLog
from celery import shared_task
from daily2.drive import save_file
from ebisuu_ai.helpers import BulkCreateManager
from ebisuu_ai.models import AILabels


@shared_task
def upload_product(dominio, book, user):
    """
    Esta tarea actualiza los productos, sus categorias y sus precios a partir de la
    carga de un archivo de una hoja de calculo.

    Parameters
    ----------
    dominio: int
        entero que representa el de los articulos que
    book: obj
        objeto del tipo xlrd que contiene todos los registros de articulos a procesar
    user : int
        entero ID del usuario que ejecuta la acción de cargar los articulos
    uid : uuid
        identificador universal único para la transacción del lote de etiquetas
    """

    subject = _("Reporte de Carga de Lote de Etiquetas")
    data_str = "Etiqueta,Procesado,Observación\n"

    country_obj = Country.objects.get(pk=country)
    user_obj = User.objects.get(pk=user)

    # LOGGER.info(msg=_("Actualizando el objeto TransactionFileLog"))
    transaction_obj = TransactionFileLog.objects.get(transaction_id=uid)
    transaction_obj.status = 1
    transaction_obj.save()

    # LOGGER.info(msg=_("Almacenando masivamente los valores del archivo"))
    sheet = book.sheet_by_index(0)
    keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]

    # LOGGER.info(msg=keys)

    bulk_mgr = BulkCreateManager(chunk_size=20)
    for row_index in range(1, sheet.nrows):
        label = sheet.cell(row_index, 0).value.upper().replace(" ", "")
        if not AILabels.objects.filter(label=label).exists():
            bulk_mgr.add(
                AILabels(
                    country=country_obj,
                    label=label,
                    real_name=sheet.cell(row_index, 1).value.upper().replace(" ", ""),
                    user=user_obj,
                )
            )
            data_str += "{},Si,Procesado exitosamente\n".format(label)
        else:
            data_str += "{},No,Esta etiqueta ya existe\n".format(label)

    bulk_mgr.done()

    message = _(
        "Se han procesado {} registros del archivo de carga de etiquetas.<br> Por favor revise el archivo adjunto para ver el resultado del proceso".format(
            sheet.nrows
        )
    )
    # LOGGER.info(msg=message)
    # LOGGER.info(msg=_("Preparando las variables para enviar el correo"))
    today = date.today()
    filename = "file_log_label_{}.csv".format(today.strftime("%y%m%d"))

    # LOGGER.info(msg=_("Preparando el archivo de resultados"))
    output = BytesIO()

    data_str = data_str.encode("utf-8")
    output.write(data_str)
    output.seek(0)

    file_url = save_file(output, filename)

    array_mail = {
        "subject": subject,
        "to": user_obj.email,
        "message": message,
        "name_report": subject,
        "filename_report": filename,
        "file_url": file_url,
    }
    SednMailCelery(array_mail)

    return True

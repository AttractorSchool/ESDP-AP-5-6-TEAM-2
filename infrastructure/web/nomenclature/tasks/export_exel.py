from celery_progress.backend import ProgressRecorder
from core import celery_app
from .base import BaseTask
from services.nomenclature_services import NomenclatureService


class ExportExcelTask(BaseTask):
    name = "ExportExcelTask"

    def run(self, nomenclature_pk, extension, *args, **kwargs):
        progress_recorder = ProgressRecorder(self)
        nomenclatures = NomenclatureService.get_all_nomenclatures()
        if nomenclatures:
            for i, nomenclature in enumerate(list(nomenclatures)):
                if int(nomenclature_pk) == nomenclature.id:
                    if nomenclature.services:
                        total_record = len(nomenclature.services)
                        for k, services in enumerate(nomenclature.services):
                            progress_recorder.set_progress(k + 1, total=total_record,
                                                           description="Inserting record into row")
                        json = {'main_data': nomenclature.services, 'extension': extension}
                        return json
                    else:
                        json = {'main_data': False, 'extension': extension}
                        return json

        else:
            json = {'main_data': False, 'extension': extension}
            return json


@celery_app.task(bind=True, base=ExportExcelTask)
def export_exel_file(self, *args, **kwargs):
    return super(type(self), self).run(*args, **kwargs)
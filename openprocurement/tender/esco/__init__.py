# -*- coding: utf-8 -*-
from openprocurement.tender.esco.models import (
    TenderESCOUA, TenderESCOEU, TenderESCOReporting
)


def includeUA(config):
    config.add_tender_procurementMethodType(TenderESCOUA)
    config.scan("openprocurement.tender.esco.views")


def includeEU(config):
    config.add_tender_procurementMethodType(TenderESCOEU)
    config.scan("openprocurement.tender.esco.views")


def includeReporting(config):
    config.add_tender_procurementMethodType(TenderESCOReporting)
    config.scan("openprocurement.tender.esco.views")
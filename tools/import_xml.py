# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BigIDocCadastre
                                 A QGIS plugin
 программа для формирования межевх и технических планов
                              -------------------
        begin                : 2016-08-04
        git sha              : $Format:%H$
        copyright            : (C) 2016 by OKSoft
        email                : olegk1980@mail.ru
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os.path, sys
import platform
from lxml import etree
from common import *

class ImportXML():
    def __init__(self, msg_log):
        self.msgLog = msg_log
        self.fileXML = ''
        self.fileXSD = ''

    def validate_schema_xml(self):
        self.msgLog(u'Определяем схему XML ...',0)
                
        for schema_xml in schemas_xml:
            xmlschema_doc = etree.parse(os.path.abspath(schemas_xml[schema_xml]['name']))
            xmlschema = etree.XMLSchema(xmlschema_doc)
            doc = etree.parse(self.fileXML)
            if xmlschema.validate(doc):
                self.fileXSD = schema_xml
                break
        
        if self.fileXSD == '':
            self.msgLog(u'Неудалось определить схему XML импорт объектов не возможен!!!',0)
        else:
            self.msgLog(u'Схема разбора XML: ' + self.fileXSD,0)
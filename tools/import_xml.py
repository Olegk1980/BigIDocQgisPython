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
import lxml.sax as sax
import os.path, sys
import platform

class ImportXML():
    def __init__(self, msgLog):
        self.msgLog = msgLog
        self.msgLog.logMessage(u'Определяем схему XML ...', 'BigiDocCadastre', self.msgLog.INFO)
        try:
            get_version_xsd()
        except Exception as err:
            self.msgLog.logMessage(u'Ошибка: '+err, 'BigiDocCadastre', level=self.msgLog.WARNING)

    def get_version_xsd():
        xsd_schema = dict(V05_STD_KPT = {name = u'\\schem\\V05_STD_KPT\\STD_KPT.xsd', uri = ''},
                          V06_STD_KPT = {name = u'\\schem\\V06_STD_KPT\\STD_KPT.xsd', uri = ''},
                          V07_STD_KPT = {name = u'\\schem\\V07_STD_KPT\\STD_KPT.xsd', uri = ''},
                          V08_STD_KPT = {name = u'\\schem\\V08_STD_KPT\\STD_KPT.xsd', uri = ''},
                          
        )
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
# import os
# from PyQt4 import QtGui, uic
# from qgis.core import *
# from qgis.gui import *


from PyQt4 import uic
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.core import *
from qgis.gui import *

# from datetime import *
# from common import *

import xml.etree.ElementTree as ET
import uuid
import os.path, sys
import platform

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'import_xml_dialog.ui'))


class ImportXML(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(ImportXML, self).__init__()
        self.setupUi(self)
        self.closeButton.clicked.connect(self.close_dialog)
        self.selectFileButton.clicked.connect(self.select_xml_file)

################################################################################

    def select_xml_file(self):
        file_xml = QFileDialog.getOpenFileName(self, u'Выбирете XML', "", '*.xml')

################################################################################
    def close_dialog(self):
        self.close()
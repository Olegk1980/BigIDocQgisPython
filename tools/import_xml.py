# -*- coding: utf-8 -*-
'''
/***************************************************************************
 importXML for openland (cadastral engineer tools)
 copyright            : (C) 2012 by Dmitriy Biryuchkov
 email                : biryuchkov@gmail.com
 ***************************************************************************/
'''
#import os
#from PyQt4 import QtGui, uic
#from qgis.core import *
#from qgis.gui import *


from PyQt4 import QtGui, uic
from PyQt4.QtCore import *
from qgis.core import *
from qgis.gui import *

#from datetime import *
#from common import *

import xml.etree.ElementTree as ET
import uuid
import os.path, sys
import platform




FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'import_xml_dialog.ui'))

class ImportXML(QtGui.QDialog, FORM_CLASS):

    def __init__(self, parent=None):
        super(ImportXML, self).__init__()
        self.setupUi(self)

# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BigIDocCadastre
                                 A QGIS plugin
 программа для формирования межевх и технических планов
                             -------------------
        begin                : 2016-08-04
        copyright            : (C) 2016 by OKSoft
        email                : olegk1980@mail.ru
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load BigIDocCadastre class from file BigIDocCadastre.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .bigidoc_cadastre import BigIDocCadastre
    return BigIDocCadastre(iface)

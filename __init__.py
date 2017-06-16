# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BigIDocCadastre
                                 A QGIS plugin
 программа для формирования межевых и технических планов
                             -------------------
        begin                : 2016-08-04
        copyright            : (C) 2016 by OKSoft
        email                : olegk1980@mail.ru
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   Эта программа является бесплатным программным обеспечением,           *
 *   Вы можете перераспределить его и / или изменить                       *
 *   В соответствии с условиями GNU General Public License, опубликованной *
 *   Фонд свободного программного обеспечения; Либо версии 2 Лицензии,     *
 *   либо (По вашему выбору) любой более поздней версии.                   *
 *                                                                         *
 ***************************************************************************/
 Этот скрипт инициализирует плагин, предоставляя его известному QGIS.
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

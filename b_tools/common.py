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

""" Словари """

# Пути к схемам
schemas_xml = {}
schemas_xml['V05_STD_KPT'] = {'name':'..//b_schem//V05_STD_KPT//STD_KPT.xsd','uri':''}
schemas_xml['V06_STD_KPT'] = {'name':'..//b_schem//V06_STD_KPT//STD_KPT.xsd','uri':''}
schemas_xml['V07_STD_KPT'] = {'name':'..//b_schem//V07_STD_KPT//STD_KPT.xsd','uri':''}
schemas_xml['V08_STD_KPT'] = {'name':'..//b_schem//V08_STD_KPT//STD_KPT.xsd','uri':''}
schemas_xml['KPT_09'] = {'name':'..//b_schem//KPT_v09//KPT//KPT_v09.xsd','uri':'urn://x-artefacts-rosreestr-ru/outgoing/kpt/9.0.3'}
schemas_xml['KPT_10'] = {'name':'..//b_schem//KPT_v10//KPT//KPT_v10.xsd','uri':'urn://x-artefacts-rosreestr-ru/outgoing/kpt/10.0.1'}
schemas_xml['V03_STD_Region_Cadastr_KV'] = {'name':'..//b_schem//V03_STD_Region_Cadastr_KV//STD_Region_Cadastr_KV.xsd','uri':''}
schemas_xml['V04_STD_Region_Cadastr_KV'] = {'name':'..//b_schem//V04_STD_Region_Cadastr_KV//STD_Region_Cadastr_KV.xsd','uri':''}
schemas_xml['V05_STD_Region_Cadastr_KV'] = {'name':'..//b_schem//V05_STD_Region_Cadastr_KV//STD_Region_Cadastr_KV.xsd','uri':''}
schemas_xml['KVZU_v06'] = {'name':'..//b_schem//KVZU_v06//KVZU//KVZU_v06.xsd','uri':'urn://x-artefacts-rosreestr-ru/outgoing/kvzu/6.0.9'}
schemas_xml['KVZU_v07'] = {'name':'..//b_schem//KVZU_v07//KVZU//KVZU_v07.xsd','uri':'urn://x-artefacts-rosreestr-ru/outgoing/kvzu/7.0.1'}
schemas_xml['KPZU_v06'] = {'name':'..//b_schem//KPZU_v06//KPZU//KPZU_v06.xsd','uri':'urn://x-artefacts-rosreestr-ru/outgoing/kpzu/6.0.1'}

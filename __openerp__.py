# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################


{
    "name": "ElectroPB",
    "icon": "/Modulo_PrickBreakers/static/img/icon.png",
    #"css": ['/Modulo_PrickBreakers/static/src/css/electroPB.css'],
    "version": "0.1",
    "category": "",
    "depends": [
                'base',
                ],
    "author": "PrickBreakers",
    "description": "Módulo para gestionar empleados de una empresa de electrodomésticos",
    "init_xml": [],
    "data": [
             'electroPB_view.xml'
             ],
    "demo_xml": [],
    "installable": True,
    "active": False,
}

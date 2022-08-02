

# -*- coding: utf-8 -*-
###############################################################################
#
#    Alejandro del Rio ( adelriocastillo@gmail.com)
#
#    Copyright (c) All rights reserved:
#        (c) 2017  TM_FULLNAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
#    Odoo and OpenERP is trademark of Odoo S.A.
#
###############################################################################
{
    'name': 'Automovile suman curse',
    'summary': 'Is a programing automovil curso',
    'version': '15.0.1.0',

    'description': """
Automovil Module Proyect.
==============================

* Caracteristica 1
* Caracteristica 2

    """,

    'author': 'GBW',
    'maintainer': 'Alejandro del Rio ',
    'contributors': ['Alejandro del Rio  <adelriocastillo@gmail.com>'],


    'website': 'http://www.gbw.com.mx',

    'license': 'AGPL-3',
    'category': 'Instruction  curse',

    'depends': [
        'base'
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'views/automovil_views.xml',
    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True
}

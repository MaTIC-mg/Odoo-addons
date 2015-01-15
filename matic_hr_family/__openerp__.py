#-*- coding:utf-8 -*-
#
#
#    Copyright (C) 2014, MaTIC - Madagascar Technologies de l'Information et de la Communication
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

{
    'name': 'Information Familiale',
    'version': '1.0',
    'category': 'Generic Modules/Human Resources',
    'description': """
Employee Family Information
===========================

    Enter extra information about employee's family
    """,
    'author': 'MaTIC - Madagascar Technologies de l\'Information et de la Communication',
    'website': 'http://www.matic.mg',
    'depends': [
        'hr',
    ],
    'init_xml': [
    ],
    'update_xml': [
        'security/ir.model.access.csv',
        'hr_view.xml',
    ],
    'test': [
    ],
    'demo_xml': [
    ],
    'installable': True,
    'active': False,
}

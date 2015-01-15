# -*- coding: utf-8 -*-
{
    'name': 'Région de Madagascar',
    'version': '1.0',
    'category': 'base',
    'description':"""
Add Malagasy states data
======================

Functionnalities :
------------------
    * Populate the table res_country_state with the madagascar states. (named 'Région')


Contacts :
----------
    * Roland Harimbola RALAIARIMANGA ; 
    * <roland.ralaiarimanga@matic.mg> for any help or question about this module.
    """,
    'author': 'MaTIC - Madagascar Technologies de l\'information et de la Commucation',
    'website': 'http://www.matic.mg',
    'license': 'AGPL-3',
    'depends': [
        'base',
        ],
    'init_xml': [],
    'update_xml': [
        'data/res_country_state_data.yml',
        ],
    'demo_xml': [],
    'js': [],
    'css': [],
    'qweb': [],
    'images': [],
    'post_load': '',
    'application': False,
    'installable': True,
    'auto_install': False,
    'images': ['static/src/img/screenshots/1.png'],
}

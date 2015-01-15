# -*- coding: utf-8 -*-
{
    'name': 'District de Madagascar',
    'version': '1.0',
    'category': 'base',
    'description': """
Add Malagasy District data
===========================

Functionnalities :
------------------
    * Create a new model res_country_district, sub division of the res_country_state ; 
    * Populate the table res_country_district with the Malagasy district ; 


Contacts :
----------
    * Roland Harimbola RALAIARIMANGA ; 
    * <roland.ralaiarimanga@matic.mg> for any help or question about this module.
    """,
    'author': 'MaTIC - Madagascar Technologies de l\'Information et de la Communication',
    'website': 'http://www.matic.mg',
    'license': 'AGPL-3',
    'depends': [
        'matic_l10n_mg_res_state',
        ],
    'init_xml': [],
    'update_xml': [
        'security/ir.model.access.csv',
        'data/res_country_district_mg_data.yml',
        'view/res_country_district_view.xml',
        'view/res_country_district_action.xml',
        'view/res_country_district_menu.xml',
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

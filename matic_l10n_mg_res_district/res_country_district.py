# -*- coding: utf-8 -*-

from openerp.osv import fields
from openerp.osv.orm import Model

class res_country_district(Model):
    _description="Country district"
    _name = 'res.country.district'

    _columns = {
        'country_state_id': fields.many2one('res.country.state', 'State',
            required=True),
        'country_id': fields.related('country_state_id', 'country_id', 
            type='many2one', relation='res.country', string='Country', 
            help="Country of the state"),
        'name': fields.char('District Name', size=128, required=True, 
                            help='Administrative divisions of District'),
        'code': fields.char('District Code', size=5,
            help='The district code in max. five chars.', required=True),
    }


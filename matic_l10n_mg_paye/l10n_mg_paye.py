from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp

class hr_contract(osv.osv):
    _inherit = 'hr.contract'

    _columns = {
        'categorie': fields.char('Categorie Professionnel', size=64),
        'echellon': fields.char('Echellon', size=64),
        'indice': fields.integer('Indice', size=10),
        'horaire_hebdo': fields.float('Horaire hébdomadaire',digits_compute=dp.get_precision('Payroll')),
	'payment_mode': fields.selection([('VIREMENT', 'VIREMENT'),('ESPECE', 'ESPECE')], 'Mode de paiement'),
    }
hr_contract()



class res_company(osv.osv):
    _inherit = 'res.company'

    _columns = {
        'seuil_irsa': fields.float('Seuil IRSA', digits_compute=dp.get_precision('Payroll')),
        'taux_irsa': fields.float('Taux IRSA', digits_compute=dp.get_precision('Payroll')),
        'abat_irsa': fields.float('Abattement IRSA', digits_compute=dp.get_precision('Payroll')),
        'cotisation_cnaps_patr': fields.float('Cotisation Patronale CNAPS', digits_compute=dp.get_precision('Payroll')),
        'cotisation_cnaps_emp': fields.float('Cotisation Employé CNAPS', digits_compute=dp.get_precision('Payroll')),
        'plafond_cnaps': fields.float('Plafond de la Securite Sociale', digits_compute=dp.get_precision('Payroll')),
        'num_cnaps_patr': fields.char('N° CNAPS', size=64),
        'cotisation_sante_patr': fields.float('Cotisation Patronale Santé', digits_compute=dp.get_precision('Payroll')),
        'cotisation_sante_emp': fields.float('Cotisation Employé Santé', digits_compute=dp.get_precision('Payroll')),
        'org_sante': fields.char('Organisme sanitaire', size=64),
        'conge_mens': fields.float('Nombre de jour congé mensuel', digits_compute=dp.get_precision('Payroll')),
    }

res_company()

class hr_employee(osv.osv):
    _inherit = 'hr.employee'
	
	
    _columns = {
		'num_cnaps_emp':fields.integer('N° CNAPS', size=10),
        'num_emp':fields.char('N° Matricule', size=64),
        'num_cin':fields.char('N° CIN', size=64),
	}
hr_employee()

		
		
		
		
		
		
		
		
		
		
	

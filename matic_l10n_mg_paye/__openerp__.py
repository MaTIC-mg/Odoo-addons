{
    'name': 'Madagascar - Gestion de la Paie',
    'category': 'Localization/Payroll',
    'author': 'MaTIC - Madagascar Technologies de l\'Information et de la Communication',
    'website': 'http://www.matic.mg',
    "category" : "Localization",
    'version': '1.0',
    'depends': ['hr_payroll'],
    
	
    'description': """Madagascar Payroll Rules.
======================

   Gestion de la Paie Malgache:     
    - Gestion des employés.
    - Gestion des contrats.
    - Configuration et paramètrage
            * Les rubriques de paie :primes,indemnités,avantages,déductions,...
            * Les rubriques cotisable ,imposable , soumise à la prime d'ancienneté  ...
            * Les cotisations : cotisations salariales et patronales CNAPS,Mutuelle...
            * Barème de la prime d'ancienneté,cotisations CNAPS ...       
    - Calcul de paie selon les normes malagasy : calcul automatique de la prime d'ancienneté,heures supplémentaire,cotisations salariales et patronales,...
    - Gestion des congés  :Calcul automatique des congés non payés à partir du module hr_holidays
    - Comptabilisation de la paie :  configuration des comptes de credit et de débit
    - Reporting : les  bulletins de paie,journale de paie ,Ordres de virement ...

Contacts :
----------
    * Roland Harimbola RALAIARIMANGA ; 
    * <roland.ralaiarimanga@matic.mg> for any help or question about this module.
    """,
    'active': False,
    'update_xml':['l10n_mg_paye_view.xml'],
    'data': [
        'l10n_mg_paye_view.xml',
        'l10n_mg_paye_data.xml',
		
    ],
    'auto_install': False,
    'installable': True,
    'application': False,
	

}

from openerp.report import report_sxw

class irsa_parser(report_sxw.rml_parse):

	def __init__(self, cr, uid, name, context):
		super(irsa_parser, self).__init__(cr, uid, name, context)
		self.localcontext.update({
		'get_irsa': self.get_irsa,
		'get_payslip_lines': self.get_payslip_lines,
		})
	def get_payslip_lines(self, objs):
		payslip_line = self.pool.get('my_report_irsa')
		res = []
		ids = []
		for item in objs:
			ids.append(item.id)
		if ids:
			res = payslip_line.browse(self.cr, self.uid, ids)
		return res
	def get_irsa(self,objs):
		sql="""select p.employee_id as id,date_from,date_to,emp.num_emp,emp.num_cin,emp.num_cnaps_emp,emp.name_related,(select total from hr_payslip_line pl where pl.slip_id=p.id AND pl.code='BASIC') as basic,(select total from hr_payslip_line pl where pl.slip_id=p.id AND pl.code='OMSI_EMP')as omsi,(select total from hr_payslip_line pl where pl.slip_id=p.id AND pl.code='OMSI_PAT')as omsiemp,(select total from hr_payslip_line pl where pl.slip_id=p.id AND pl.code='CNAPS_EMP')as cnaps,(select total from hr_payslip_line pl where pl.slip_id=p.id AND pl.code='CNAPS_PAT')as cnapsemp,(select total from hr_payslip_line pl where pl.slip_id=p.id AND pl.code='GROSS')as brut,(select total from hr_payslip_line pl where pl.slip_id=p.id AND pl.code='IRSA')as irsa,(select total from hr_payslip_line pl where pl.slip_id=p.id AND pl.code='NET')as net from hr_payslip p inner join hr_employee emp on p.employee_id=emp.id where emp.num_emp=%s""",[objs]
		self.cr.execute(sql)
		res=self.cr.dictfetchall()
		return res
report_sxw.report_sxw('report.irsa', 'my.report.irsa', 'matic_l10n_mg_paye/report/rapport_irsa.rml', parser=irsa_parser)
from __future__ import unicode_literals
import frappe
from frappe import _

data = {
		'custom_fields':{ 
				"Sales Invoice":[
        {
					"fieldname": "section_section101",
					"fieldtype": "Section Break",
					"insert_after": "set_target_warehouse",
					"label": _("Cars Detials"),
				},
				{
					"fieldname": "plate_number",
					"fieldtype": "Data",
					"insert_after": "section_section101",
					"label": _("Plate Number"),
				},
        ]

		},
			"properties": [

		],
	
}


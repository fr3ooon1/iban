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
        {
					"fieldname": "car_color",
					"fieldtype": "Data",
					"insert_after": "plate_number",
					"label": _("Car Color"),
				},
        {
					"fieldname": "column_break101",
					"fieldtype": "Column Break",
					"insert_after": "car_color",
				},
        {
					"fieldname": "car_type",
					"fieldtype": "Data",
					"insert_after": "column_break101",
					"label": _("Car Type"),
				},
        {
					"fieldname": "installed_order",
					"fieldtype": "Data",
					"insert_after": "car_type",
					"label": _("Installed Order"),
				},
        {
					"fieldname": "column_section102",
					"fieldtype": "Column Break",
					"insert_after": "installed_order",
				},
        {
					"fieldname": "notes",
					"fieldtype": "Small Text",
					"insert_after": "column_section102",
					"label": _("Notes"),
				},
        ],
                "Quotation":[
        {
					"fieldname": "car_section",
					"fieldtype": "Section Break",
					"insert_after": "ignore_pricing_rule",
					"label": _("Cars Detials"),
				},
				{
					"fieldname": "plate_number",
					"fieldtype": "Data",
					"insert_after": "car_section",
					"label": _("Plate Number"),
				},
        {
					"fieldname": "car_color",
					"fieldtype": "Data",
					"insert_after": "plate_number",
					"label": _("Car Color"),
				},
        {
					"fieldname": "car_column_break1",
					"fieldtype": "Column Break",
					"insert_after": "car_color",
				},
        {
					"fieldname": "car_type",
					"fieldtype": "Data",
					"insert_after": "car_column_break1",
					"label": _("Car Type"),
				},
        {
					"fieldname": "installed_order",
					"fieldtype": "Data",
					"insert_after": "car_type",
					"label": _("Installed Order"),
				},
        {
					"fieldname": "car_column_break2",
					"fieldtype": "Column Break",
					"insert_after": "installed_order",
				},
        {
					"fieldname": "notes",
					"fieldtype": "Small Text",
					"insert_after": "car_column_break2",
					"label": _("Notes"),
				},
        ]

		},
			"properties": [

		],
	
}


// Copyright (c) 2025, Gary Gabriel Garcia Cruz and contributors
// For license information, please see license.txt

frappe.query_reports["Reporte de ventas LCDP"] = {
	   filters: [
        {
            fieldname: "fecha_inicio",
            label: "Fecha de inicio",
            fieldtype: "Date",
            default: frappe.datetime.get_today()
        },
        {
            fieldname: "fecha_fin",
            label: "Fecha de fin",
            fieldtype: "Date",
            default: frappe.datetime.get_today()
        }
    ]
};

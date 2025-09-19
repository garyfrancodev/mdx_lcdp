import frappe
from frappe import _

def execute(filters=None):
    columns = [
        {"label": _("Fecha"), "fieldname": "transaction_date", "fieldtype": "Date"},
        {"label": _("Orden de Venta"), "fieldname": "name", "fieldtype": "Link", "options": "Sales Order"},
        {"label": _("Cliente"), "fieldname": "customer", "fieldtype": "Link", "options": "Customer"},
        {"label": _("Tax ID"), "fieldname": "tax_id", "fieldtype": "Data"},
        {"label": _("Total"), "fieldname": "grand_total", "fieldtype": "Currency"},
        {"label": _("Total Pagado"), "fieldname": "total_pagado", "fieldtype": "Currency"},
        {"label": _("Saldo por Cobrar"), "fieldname": "saldo_por_cobrar", "fieldtype": "Currency"},
        {"label": _("Nota de Entrega"), "fieldname": "nota_entrega", "fieldtype": "Data"},
    ]

    where = ["so.docstatus = 1"]
    params = {}

    if filters:
        if filters.get("fecha_inicio"):
            where.append("so.transaction_date >= %(fecha_inicio)s")
            params["fecha_inicio"] = filters["fecha_inicio"]
        if filters.get("fecha_fin"):
            where.append("so.transaction_date <= %(fecha_fin)s")
            params["fecha_fin"] = filters["fecha_fin"]

    where_clause = "WHERE " + " AND ".join(where)

    data = frappe.db.sql(f"""
        SELECT
            so.name,
            so.customer,
            c.tax_id,
            so.transaction_date,
            so.status,
            so.grand_total,
            IFNULL((
                SELECT SUM(pei.allocated_amount)
                FROM `tabPayment Entry Reference` pei
                INNER JOIN `tabPayment Entry` pe ON pe.name = pei.parent
                WHERE pei.reference_doctype = 'Sales Order'
                  AND pei.reference_name = so.name
                  AND pe.docstatus = 1
            ), 0) AS total_pagado,
            (so.grand_total - IFNULL((
                SELECT SUM(pei.allocated_amount)
                FROM `tabPayment Entry Reference` pei
                INNER JOIN `tabPayment Entry` pe ON pe.name = pei.parent
                WHERE pei.reference_doctype = 'Sales Order'
                  AND pei.reference_name = so.name
                  AND pe.docstatus = 1
            ), 0)) AS saldo_por_cobrar,
            CASE WHEN EXISTS (
                SELECT 1 FROM `tabDelivery Note Item` dni
                WHERE dni.against_sales_order = so.name
                  AND dni.docstatus = 1
            ) THEN 'Sí' ELSE 'No' END AS nota_entrega
        FROM `tabSales Order` so
        LEFT JOIN `tabCustomer` c ON so.customer = c.name
        {where_clause}
        ORDER BY so.transaction_date DESC
    """, params, as_dict=1)
    return columns, data
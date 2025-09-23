import frappe

def generar_nota_entrega_si_tikeado(doc, method):
    if getattr(doc, "custom_generar_nota_de_entrega", None):
        try:
            dn = frappe.get_doc({
                "doctype": "Delivery Note",
                "customer": doc.customer,
                "items": [
                    {
                        "item_code": item.item_code,
                        "qty": item.qty,
                        "so_detail": item.name,
                        "sales_order": doc.name,
                        "against_sales_order": doc.name  # <-- Agrega esta línea si el campo existe
                    }
                    for item in doc.items
                ],
                "company": doc.company,
                "posting_date": frappe.utils.nowdate(),
                "set_warehouse": getattr(doc, "set_warehouse", None)
            })
            dn.insert()
            dn.submit()
            frappe.msgprint(
                f"""<b>Nota de Entrega generada:</b> <a href="/app/delivery-note/{dn.name}" target="_blank">{dn.name}</a>""",
                title="Nota de Entrega Automática",
                indicator="green"
            )
        except Exception as e:
            frappe.msgprint(f"Error al generar la Nota de Entrega: {e}", indicator="red")
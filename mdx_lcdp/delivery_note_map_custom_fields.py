import frappe

def set_custom_fields_on_delivery_note(doc, method):
    # Solo ejecuta si la nota de entrega fue creada desde una orden de venta
    if doc.get("sales_order"):
        for item in doc.items:
            # Busca el Sales Order Item original
            so_item = frappe.db.get_value(
                "Sales Order Item",
                {"name": item.so_detail},
                ["custom_cantidad_m2", "custom_precio_m2"],
                as_dict=True
            )
            if so_item:
                item.custom_cantidad_m2 = so_item.custom_cantidad_m2
                item.custom_precio_m2 = so_item.custom_precio_m2
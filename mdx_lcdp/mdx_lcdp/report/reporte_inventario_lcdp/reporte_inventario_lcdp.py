import frappe

def execute(filters=None):
    filters = filters or {}

    # Obtener la primera lista de precios activa de tipo "Selling"
    price_list_name = frappe.db.get_value("Price List", {"selling": 1, "enabled": 1}, "name")

    columns = [
        {"label": "Código", "fieldname": "item_code", "fieldtype": "Link", "options": "Item", "width": 80},
        {"label": "Nombre del artículo", "fieldname": "item_name", "fieldtype": "Data", "width": 330},
        {"label": "Grupo de Producto", "fieldname": "item_group", "fieldtype": "Link", "options": "Item Group", "width": 150},
        {"label": "Cantidad", "fieldname": "qty", "fieldtype": "float", "width": 90},
        {"label": "UM", "fieldname": "stock_uom", "fieldtype": "Link", "options": "UOM", "width": 100},
        {"label": "Precio de Venta", "fieldname": "price", "fieldtype": "Currency", "width": 170},
        {"label": "Cantidad (m2)", "fieldname": "alt_qty", "fieldtype": "Float", "width": 130},
        {"label": "UM alternativa", "fieldname": "alt_uom", "fieldtype": "Link", "options": "UOM", "width": 130},
        
    ]

    data = []

    filters_bin = {"actual_qty": [">", 0]}
    if filters.get("item_code"):
        filters_bin["item_code"] = filters["item_code"]

    bins = frappe.get_all("Bin",
        fields=["item_code", "warehouse", "actual_qty"],
        filters=filters_bin
    )

    for b in bins:
        item = frappe.get_doc("Item", b.item_code)

        if filters.get("item_name") and filters["item_name"].lower() not in item.item_name.lower():
            continue

        stock_uom = item.stock_uom
        item_name = item.item_name
        item_group = item.item_group

        # Obtener precio desde la lista dinámica
        price = frappe.db.get_value("Item Price", {
            "item_code": b.item_code,
            "price_list": price_list_name
        }, "price_list_rate") or 0

        alt_qty = 0
        alt_uom = ""

        for uom in item.uoms:
            if uom.uom != stock_uom:
                alt_uom = uom.uom
                if uom.conversion_factor:
                    alt_qty = b.actual_qty * uom.conversion_factor
                break

        data.append({
            "item_code": b.item_code,
            "item_name": item_name,
            "item_group": item_group,
            "qty": b.actual_qty,
            "stock_uom": stock_uom,
            "alt_qty": alt_qty,
            "alt_uom": alt_uom,
            "price": price,
            
        })

    return columns, data

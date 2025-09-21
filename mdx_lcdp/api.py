import frappe

@frappe.whitelist()
def actualizar_precios_masivo(price_list, porcentaje):
    porcentaje = float(porcentaje)
    productos = frappe.get_all("Item", filters={"disabled": 0}, fields=["name"])
    productos_activos = set([p.name for p in productos])

    items = frappe.get_all("Item Price", filters={"price_list": price_list}, fields=["name", "item_code", "price_list_rate"])
    item_codes_con_precio = set([item.item_code for item in items])

    faltantes = productos_activos - item_codes_con_precio

    if faltantes:
        mensaje = f"""
        <h3 style='color:#d9534f;'>Actualización de precios fallida</h3>
        <ul>
            <li><b>Productos activos:</b> {len(productos_activos)}</li>
            <li><b>Productos actualizados:</b> 0</li>
            <li><b>Productos no actualizados:</b> {len(faltantes)}</li>
        </ul>
        <p style='color:#d9534f;'><b>Los siguientes productos no tienen precio en la lista seleccionada:</b></p>
        <div style='max-height:120px;overflow:auto;border:1px solid #eee;padding:5px;background:#f9f9f9;'>{', '.join(faltantes)}</div>
        """
        # Registrar en el timeline
        frappe.get_doc("Price List", price_list).add_comment(
            "Info",
            f"Actualización masiva fallida. Porcentaje: {porcentaje}%. "
            f"Productos actualizados: 0. Productos no actualizados: {len(faltantes)}."
        )
        return mensaje

    for item in items:
        if item.price_list_rate is not None:
            nuevo_precio = item.price_list_rate * (1 + porcentaje / 100)
            frappe.db.set_value("Item Price", item.name, "price_list_rate", nuevo_precio)

    mensaje = f"""
    <h3 style='color:#5cb85c;'>Actualización exitosa</h3>
    <ul>
        <li><b>Lista de precios:</b> {price_list}</li>
        <li><b>Porcentaje aplicado:</b> {porcentaje}%</li>
        <li><b>Productos activos:</b> {len(productos_activos)}</li>
        <li><b>Productos actualizados:</b> {len(productos_activos)}</li>
        <li><b>Productos no actualizados:</b> 0</li>
    </ul>
    """
    # Registrar en el timeline
    frappe.get_doc("Price List", price_list).add_comment(
        "Info",
        f"Actualización masiva exitosa. Porcentaje: {porcentaje}%. "
        f"Productos actualizados: {len(productos_activos)}. Productos no actualizados: 0."
    )
    return mensaje
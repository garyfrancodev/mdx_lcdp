frappe.query_reports["Reporte inventario LCDP"] = {
    formatter: function(value, row, column, data, default_formatter) {
        value = default_formatter(value, row, column, data);

        if (column.fieldname === "qty" && data && data.qty > 0) {
            value = `<span style="color:green;">${value}</span>`;
        }

        if (column.fieldname === "item_code" && data && data.item_code) {
            // Solo mostrar el código y mantener el link al producto
            value = `<a href="/app/item/${data.item_code}" target="_blank">${data.item_code}</a>`;
        }

        return value;
    }
};
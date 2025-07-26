frappe.query_reports["Reporte inventario LCDP"] = {
    formatter: function(value, row, column, data, default_formatter) {
        value = default_formatter(value, row, column, data);

        if (column.fieldname === "qty" && data && data.qty > 0) {
            value = `<span style="color:green;">${value}</span>`;
        }

        return value;
    }
};

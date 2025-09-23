app_name = "mdx_lcdp"
app_title = "Mdx Lcdp"
app_publisher = "Gary Gabriel Garcia Cruz"
app_description = "Parametrizacion exclusiva para importadora de Porcelanatos"
app_email = "garcia.cruzgc@gmail.com"
app_license = "mit"

doc_events = {
    "Sales Order": {
        "on_submit": "mdx_lcdp.sales_order_hooks.generar_nota_entrega_si_tikeado"
    },
    "Delivery Note": {
        "before_insert": "mdx_lcdp.delivery_note_map_custom_fields.set_custom_fields_on_delivery_note"
    }
}



fixtures = [
    # Aquí puedes añadir los DocTypes que quieras exportar como fixtures.
    {"dt": "Letter Head", "filters": [["name", "=", "Membrete LCDP 1.0"]]}, # este es el Membrete personalizado que se exportará.
    {"dt": "Print Settings"}, # Este es el DocType de configuraciones de impresión que se exportará.
    {"dt": "Print Format", "filters": [["name", "in", ["NT sin imagen","OV sin imagen", "Cot. sin imagen","Cot. con imagen"]]]}, # Este es el formato de impresión personalizado que se exportará.
    {"dt": "Currency", "filters": [["name", "=", "BOB"]]},  # Exporta la configuración de la moneda BOB
    {"dt": "System Settings"},
    {"dt": "Global Defaults"},
    # Unidades de medidas fijas
    {"dt": "UOM", "filters": [["uom_name", "in", ["Pieza(s)", "Caja(s)", "Paquete(s)", "m2","Balde(s)"]]]},
    # Grupos de productos fijos
    {"dt": "Item Group", "filters": [["name", "in", ["HERRAMIENTAS", "PORCELANATOS", "PERFILES", "REJILLAS"]]]},
    {"dt": "Client Script"},
    {"dt": "Account", "filters": [["name", "=", "1210 - Bancos - L"]]},
    {"dt": "Mode of Payment", "filters": [["name", "=", "QR"]]},
    {"dt": "Translation"},
    {"dt": "Custom Field", "filters": [
    ["dt", "in", ["Quotation Item", "Sales Order Item", "Sales Order", "Delivery Note Item"]],
    ["fieldname", "in", ["custom_consolidar","custom_cantidad_m2", "custom_precio_m2", "custom_generar_nota_de_entrega"]]]},
    {
    "dt": "Property Setter",
    "filters": [
        ["doc_type", "in", ["Payment Entry","Quotation Item", "Sales Order Item", "Delivery Note Item", "Customer"]],
        ["field_name", "in", ["rate", "amount", "tax_id","actual_qty", "item_code","qty","uom","delivery_date","reference_no"]],
        ["property", "in", ["columns", "reqd", "in_list_view", "default"]]
    ]
    },
]



# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "mdx_lcdp",
# 		"logo": "/assets/mdx_lcdp/logo.png",
# 		"title": "Mdx Lcdp",
# 		"route": "/mdx_lcdp",
# 		"has_permission": "mdx_lcdp.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mdx_lcdp/css/mdx_lcdp.css"
# app_include_js = "/assets/mdx_lcdp/js/mdx_lcdp.js"

# include js, css files in header of web template
# web_include_css = "/assets/mdx_lcdp/css/mdx_lcdp.css"
# web_include_js = "/assets/mdx_lcdp/js/mdx_lcdp.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "mdx_lcdp/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "mdx_lcdp/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "mdx_lcdp.utils.jinja_methods",
# 	"filters": "mdx_lcdp.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "mdx_lcdp.install.before_install"
# after_install = "mdx_lcdp.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "mdx_lcdp.uninstall.before_uninstall"
# after_uninstall = "mdx_lcdp.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "mdx_lcdp.utils.before_app_install"
# after_app_install = "mdx_lcdp.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "mdx_lcdp.utils.before_app_uninstall"
# after_app_uninstall = "mdx_lcdp.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mdx_lcdp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mdx_lcdp.tasks.all"
# 	],
# 	"daily": [
# 		"mdx_lcdp.tasks.daily"
# 	],
# 	"hourly": [
# 		"mdx_lcdp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mdx_lcdp.tasks.weekly"
# 	],
# 	"monthly": [
# 		"mdx_lcdp.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "mdx_lcdp.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mdx_lcdp.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "mdx_lcdp.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["mdx_lcdp.utils.before_request"]
# after_request = ["mdx_lcdp.utils.after_request"]

# Job Events
# ----------
# before_job = ["mdx_lcdp.utils.before_job"]
# after_job = ["mdx_lcdp.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"mdx_lcdp.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }


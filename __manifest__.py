{
    'name': "export_view_parthenay",

    'summary': """
        Module de Parthenay-Gâtine pour la base de ses développements permettant d'exporter des données dans un fichier excel""",

    'description': """
        Module Parthenay-Gâtine comprenant les différentes définitions pour les devs Parthenay.
    """,

    'author': "Communauté de communes de Parthenay-Gâtine",
    'website': "http://www.cc-parthenay-gatine.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Parthenay',
    'version': '11.0.09.11.2020',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'ecole'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/inherited_ecole_partner_school.xml',
    ],
    'qweb': [
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
}

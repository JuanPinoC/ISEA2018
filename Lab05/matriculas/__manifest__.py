# -*- coding: utf-8 -*-
{
    'name': "matriculas",

    'summary': """
        Módulo para matrículas.""",

    'description': """
        Este módulo permite gestionar las matriculas a los diferentes cursos de los alumnos.
    """,

    'author': "Juan Pino",
    'website': "http://www.acme.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/areas.xml',
        'views/cursos.xml',
        'views/matriculas.xml',
        'views/alumnos.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
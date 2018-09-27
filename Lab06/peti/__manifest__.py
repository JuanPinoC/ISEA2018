# -*- coding: utf-8 -*-
{
    'name': "PETI",

    'summary': """
        Módulo de Planeación Estrategica de TI""",

    'description': """
        Este módulo permite gestionar de acuerdo al PETI, quien(empleados) realiza que
        (tareas) y como(recursos empleados, tiempo, etc.) dentro de una empresa.""",

    'version': '0.1',

    'depends': ['base'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/areas.xml',
        'views/empleados.xml',
        'views/recursos.xml',
        'views/tareas.xml',
        'views/templates.xml',
    ],

    'installable': True
}
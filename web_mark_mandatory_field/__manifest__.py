# -*- coding: utf-8 -*-
{
    'name': "Web Mark Mandatory Field",
    'version': '18.0.0.1',
    'category': 'Hidden',
    'summary': 'A module to add asterisk in mandatory fields in form view .',
    'description': '''
            This module  to add add asterisk in form view.
        ''',
    'author': 'Amniltech Team',
    'depends':[
        'base_setup', 
    ],
    'data': [
        
    ],
     'assets': {
        'web.assets_backend': [
            'web_mark_mandatory_field/static/src/scss/mandatory_field.scss',
        ],
    },
    "license": "AGPL-3",
    'installable': True,
    'application': False,
    'auto_install': False
}

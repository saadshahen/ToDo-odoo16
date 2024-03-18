{
    'name': "To-Do",
    'author': "saad shahain",
    'category': '',
    'version': "16.0.0.1.0",
    'depends':['base', 'sale_management','account','mail',
               ],
    'data':[
        'views/base_menu.xml',
        'views/To_Do_view.xml',
        'security/ir.model.access.csv',
        'views/partner_view.xml',
    ],
    'assets': {
        'web.assets_backend': ['todo/static/src/css/todo.css']
    },

    'application':True,
}
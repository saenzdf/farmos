{
    'name': 'Set Company to Product & POS Categories',  
    'version': '1.0',
    'summary': 'Adds a company field to Product Categories and POS Categories',  
    'description': """
        This module adds a Many2one relationship with res.company to:
        - Product Categories (product.category)
        - POS Categories (pos.category)
        
        This ensures that categories are assigned to specific companies in multi-company environments.
    """,  
    'author': 'terrabloque',  
    'website': 'https://terrabloque.com',  
    'category': 'Inventory/Product Management',  
    'license': 'LGPL-3',  
    'depends': ['product', 'point_of_sale'], 
    'data': [
        'views/product_category_views.xml', 
    ],
    'installable': True,
    'application': False,
    'auto_install': False, 
}


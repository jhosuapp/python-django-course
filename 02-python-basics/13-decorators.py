# Decorators

# def require_auth(func):
#     def wrapper(user, data):
#         if(user == 'admin'):
#             print(data)
#             return func(user)
#         else: 
#             return f'Acceso denegado para {user}'
        
#     return wrapper

# @require_auth
# def admin_dashboard(user):
#     return f'Bienvenido al panel, {user}'

# print(admin_dashboard('admin', 'testdata'))
# print(admin_dashboard('invitado', 'testdata'))


min_price = 1000;
min_products = 10;

def cart(func):
    def wrapper(total_products, total_price):
        if(total_price >= min_price and total_products >= min_products):
            return func(total_products, total_price)
        elif(total_price <= (min_price - 1)):
            return f'añade mas productos para obtener un descuento, te falta {min_price - total_price}'
        elif(total_products <= (min_products - 1)):
            return f'añade mas productos para obtener un descuento {min_products - total_products}'
        else: 
            return f'No puedes acceder a ningun descuento, añade más productos'
    
    return wrapper

@cart
def discount(total_products, total_price):
    return f'Tienes un descuento y envío gratis por la compra de: {total_products} prodcutos con un total de ${total_price}'

print(discount(11, 1001))
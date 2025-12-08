# Higher order function

def require_auth(func):
    def wrapper(user, data):
        if(user == 'admin'):
            print(data)
            return func(user)
        else: 
            return f'Acceso denegado para {user}'
        
    return wrapper


def admin_dashboard(user):
    return f'Bienvenido al panel, {user}'

auth_view_dashboard = require_auth(admin_dashboard)

print(auth_view_dashboard('admin', 'testdata'))
print(auth_view_dashboard('invitado', 'testdata'))
# and 
age = 19
licensed = False

if (age >= 18 and licensed): 
    print('Puede conducir')
    
# or
is_student = False
memerbeship = True

if (is_student or memerbeship):
    print("Obtiene precio especial")
    
# not
is_admin = False

if (not is_admin):
    print("Acceso denegado.")
    
# Short circuiting

name = False
print(name and name.upper())
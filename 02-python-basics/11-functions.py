# # Parámetros
# def hello(greet, name):
#     print(f"{greet}, {name}")
    
# # Argumentos
# hello('Hola', 'Jhosua')
# hello(name='Jhos', greet='Hola')

def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return kwargs

print(big_function(1,2,3,4,5,6,7,8, num=100, num2=200))
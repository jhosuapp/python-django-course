def divide_number():
    try:
        a = int(input('Ingresa el numerador: '))
        b = int(input('Ingresa el denominador: '))
    except ZeroDivisionError:
        print('No se puede dividir entre 0.')
    except ValueError:
        print('Solo se permiten valores númericos.')
    except Exception as error:
        print(type(error))
    else: 
        result = a / b
        return print(f'El resultado es: {result}')
    finally:
        print('Gracias por usar nuestra calculadora')

divide_number()
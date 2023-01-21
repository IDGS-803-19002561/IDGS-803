
def main () : 
    optionone = int(input('Selecciona un tipo de operacion \n 1.- Suma \n 2.-Resta \n 3.-Multiplicacion \n 4.-Divicion \n 5.-Salir \n '))
    print(optionone)
    while (optionone  <  5) :
        num1 = int(input('Ingresa el valor 1 : '))
        num2 = int(input('Ingresa el valor 2 : '))
        result = operation(num1 , num2 , optionone)
        print('Resultado es : {}'.format(result))
        optionone = int(input('Selecciona un tipo de operacion 1.- Suma 2.-Resta 3.-Multiplicacion 4.-Divicion  5.-Salir '))

def operation(num1, num2, type):
    if (type == 1):
        return (num1 + num2)
    elif (type == 2):
        return (num1 - num2)
    elif (type == 3):
        return (num1 * num2)
    elif (type == 4):
        return (num1 / num2)
    else:
        return False


if __name__ == '__main__':
    main()

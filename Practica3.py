class Operacion:

    a = 0
    b = 0

    def setA(self, a):
        self.a = a

    def setB(self, b):
        self.b = b

    def suma(self):
        return self.a + self.b

    def rest(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


def main():
    obj = Operacion()

    optionone = int(input(
        'Selecciona un tipo de operacion \n 1.- Suma \n 2.-Resta \n 3.-Multiplicacion \n 4.-Divicion \n 5.-Salir \n '))
    print(optionone)

    while (optionone < 5):
        result = 0

        obj.setA(int(input('Ingresa el valor 1 : ')))
        obj.setB(int(input('Ingresa el valor 2 : ')))

        if (optionone == 1):
            result = obj.suma()
        elif (optionone == 2):
            result = obj.rest()
        elif (optionone == 3):
            result = obj.mult()
        elif (optionone == 4):
            result = obj.div()

        print('Resultado es : {}'.format(result))

        optionone = int(input(
            'Selecciona un tipo de operacion 1.- Suma 2.-Resta 3.-Multiplicacion 4.-Divicion  5.-Salir '))


if __name__ == '__main__':
    main()

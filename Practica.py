# numero hacer la tabla de multiplicacion
def getTabla(num):
    for x in range(1, 11):
        print("{} X {} = {}".format(num, x,  num * x))

num = int(input('Ingresa el numero : '))
getTabla(num)


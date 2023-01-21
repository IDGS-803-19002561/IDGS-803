dato1 = "hola"
dato2 = "mundo"

datoFinal = dato1 + " " + dato2
print(datoFinal)

saludo = "Saludo1 es: %s %s"%(dato1 , dato2)
print(saludo)

saludo = ("Saludo2 {0} {1}").format(dato1 ,dato2)
print(saludo)

saludo = ("Saludo3 {a} {b}").format(a=dato1 , b=dato2)
print(saludo)

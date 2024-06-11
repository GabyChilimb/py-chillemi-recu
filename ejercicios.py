def Punto1():
    v1 = input("Ingrese un numero.")
    v1 = int(v1)
    v2 = input("Ingrese otro numero.")
    v2 = int(v2)

    resultado = v1 + v2

    print("El resultado es: ", resultado)

#Punto1

def Punto2():
    v1 = input("Ingrese un numero.")
    v1 = int(v1)
    v2 = input("Ingrese otro numero.")
    v2 = int(v2)
    v3 = input("Ingrese otro numero.")
    v3 = int(v3)
    v4 = input("Ingrese otro numero.")
    v4 = int(v4)

    resultado = v1 + v2 + v3 + v4

    print("El resultado es: ", resultado)
#Punto2

def Punto3():
    lado1 = int(input("Cuánto mide el lado 1?"))
    lado2 = int(input("Cuánto mide el lado 2?"))

    superficie = lado1 * lado2

    print("La superficie es: ", superficie)
#Punto3

def Punto4():
    lado1 = float(input("Ponga un número con decimales."))

    superficie = lado1 * lado1

    print("La superficie es: ", superficie)
#Punto4

def Punto5():
    hora = int(input("Ponga la hora."))
    minutos = int(input("Ponga los minutos."))
    segundos = int(input("Ponga los segundos."))

    resultado1 = hora * 3600
    resultado2 = minutos *60

    EnSegundos = resultado1 + resultado2 + segundos

    print("El resultado expresado en segundos es: "+ EnSegundos)
    #Punto5

def Punto6():
    ladoA = int(input("Cuanto mide el lado a?"))
    ladoB = int(input("Cuanto mide el lado b?"))


    suptriangulo = ladoA * ladoB /2
    print("La superficie del triangulo es: "+suptriangulo)
#Punto6()

def Punto7():
    n1 = input("Ponga un número.")
    n1 = int(n1)
    n2 = input("Ponga un segundo número.")
    n2 = int(n2)
    n3 = input("Ponga un tercer número.")
    n3 = int(n3)
    n4 = input("Ponga un cuarto número.")
    n4 = int(n4)
    n5 = input("Ponga un quinto número.")
    n5 = int(n5)
    n6 = input("Ponga el último número.")
    n6 = int(n6)

    total = n1+ n2 + n3 + n4 + n5 + n6

    promedio = total/6

    print("El promedio es: "+ promedio)
#Punto7()


def Punto8():
    n1 = int(input("Ponga un número."))
    n2 = int(input("Ponga otro número."))

    numero1 = n1/100
    porcentaje = n2 / numero1

    print("El promedio es:%", porcentaje)
#Punto8()

def Punto9():
    fecha = int(input("Ingrese la fecha en formato DDMMAAAA."))

    dia = fecha//1000000
    mes = (fecha//10000) % 100
    año = fecha % 10000

    print("Día: ", dia)
    print("Mes: ", mes)
    print("Año: ", año)
#Punto9()

def Punto10():
    a = int(input("Ingrese la calificación de exámen parcial."))
    b = int(input("Ingrese la calificación por TPs."))
    c = int(input("Ingrese la calificación del exámen integrador."))

    calificacionA = a * 0.3
    calificacionB = b * 0.2
    calificacionC = c * 0.5

    notafinal = calificacionA + calificacionB + calificacionC
    print("El promedio del estudiante es: "+ notafinal)
#Punto10

def Punto11():

    autos = []
    inputUser = ""
    while inputUser != "SALIR":
        inputUser = input("ingrese el valor del auto vendido o SALIR")
        if inputUser != "SALIR":
            inputUser = float(inputUser)
            autos.append(inputUser)

    AUx = sum(autos)
    comision = AUx * 0.05

#Punto11()
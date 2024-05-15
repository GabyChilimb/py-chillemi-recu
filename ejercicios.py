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
    Punto5()
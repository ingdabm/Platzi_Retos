#Validando el tipo de Triangulo
def verificatipo(base):
    lado1 = int(input("Ingresa por favor el valor de uno de los lados: "))
    lado2 = int(input("Ingresa por favor el valor del otro lado disponible: "))
    if lado1 == base and lado1 == lado2:
        print("vaya! todos los lados son iguales, se trata de un Equilatero")
    elif lado1 != base and lado1 != lado2:
        print("vaya! todos los lados son distintos, se trata de un Escaleno")
    else:
        print("vaya! por lo menos dos lados son iguales, se trata de un Isoceles")

#Configurando el Arranque del Programa
def run (): 
    print(""" 
    Bienvenido a este programa, te ayudara calcular el area 
    de un triangulo a partir de su base y su altura 
    """)
    base = int(input("Ingresa por favor el la base del triangulo: "))
    altura = int(input("Ingresa por favor la Altura del Trian2gulo: "))
    areatriangulo = base*altura/2
    print(f'El area del Triangulo es: {areatriangulo} m2')
    print(""" 
    Puedo ayudarte a saber que tipo de triangulo es si conoces
    los otros lados del mismo, dispones de la informacion de los otros lados: 
    """)
    respuesta = int(input("Presiona 1. si conoces los otros lados, o 2 si no: "))
    if respuesta == 1: 
        verificatipo(base)
    elif respuesta == 2:
        print("nos vemos, Gracias por usar este programa")
    else:
        print("No ingresaste una opcion valida, Adios!")

if __name__ == "__main__":
    run()
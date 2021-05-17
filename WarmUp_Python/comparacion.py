def comparacion(l_inferior,l_superior,referencia):
    
    while referencia < l_inferior or referencia > l_superior:
        print("Lo lamento, tu número no se encuentra entre los rangos")
        referencia = float(input("\nPorfavor ingresa otro valor que esté entre los rangos: "))
    
    if referencia >= l_inferior and referencia <= l_superior:
        respuesta = print(f' El número {referencia} se encuentra entre el rango [{l_inferior},{l_superior}]')
    
def run():
    print('RANGOS CAMBIANTES'.center(74, '*'))
    l_superior = float(input("Ingresa por favor el Limite Superior del rango: "))
    l_inferior = float(input("Ingresa por favor el Limite inferior del rango: "))
    
    while l_inferior > l_superior:
        print(f'El limite inferior es mayor que el inferior, corrige por favor: ')
        l_superior = float(input("Ingresa por favor el Limite Superior del rango: "))
        l_inferior = float(input("Ingresa por favor el Limite inferior del rango: "))
    
    referencia = float(input("Ingresa por favor el valor de comparacion: "))
    comparacion(l_inferior, l_superior, referencia)

if __name__ == "__main__": 
    run()
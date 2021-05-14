import math

def run():
     
    print('CALCULO DE VOLUMENES'.center(74, '*'))
    msg1 = """
        → Elige el tipo de cuerpo al que quieres calcular el volumen:
        1. Cubo
        2. Cilindro
        3. Esfera 
        4. Cono 
        5. Salir
    """
    print(msg1)
    
    respuesta = int(input("Cual es tu eleccion: "))
    if respuesta == 1:
        lado = float(input("Digita el valor de uno de los lados: "))
        volumen = round(lado**3, 2)
        print(f'El volumen del cubo de lado: {lado} es {volumen}') 
    
    elif respuesta == 2:
        radio = float(input("Digita el valor del radio del Cilindro: "))
        altura = float(input("Digita el valor de la altura del Cilindro: "))
        volumen = round(math.pi*radio**2*altura, 2)
        print(f'El volumen del Cilindro de radio: {radio} y altura: {altura} es {volumen}') 
    
    elif respuesta == 3:
        radio = float(input("Digita el valor del radio de la esfera: "))
        volumen = round(4*math.pi*radio**3/3, 2)
        print(f'El volumen de la esfera de radio: {radio} es {volumen}')
    
    elif respuesta == 4:
        radio = float(input("Digita el valor del radio del cono: "))
        altura = float(input("Digita el valor de la altura del cono: "))
        volumen = round(math.pi*radio**2*altura/3, 2)
        print(f'El volumen del Cono de radio: {radio} y altura: {altura} es {volumen}') 
    
    elif respuesta == 5:
        print("OK, nos vemos")
    
    else:
        print("no elegiste una opcion valida, Adios!!!")

if __name__ == "__main__":
    run()

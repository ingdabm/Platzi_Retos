def run():
    miles_to_km = 1.609344 
    km_to_miles =  0.621371

    print('CONVERSOR DE MEDIDAS'.center(74, '*'))
    
    msg1 = """
        → Elige una opción de conversion:
        1. Convertir de Km a Millas
        2. Convertir de Millas a KM
    """
    
    print(msg1)

    respuesta = int(input('Selecciona que tipo de conversion quieres realizar: '))
    if respuesta == 1: 
        convertir = int(input('Ingresa la cantidad de Km a convertir: '))
        resultado = round(convertir*km_to_miles, 2)
        print(f'{convertir} Kms son {resultado} millas')
    elif respuesta == 2:
        convertir = int(input('Ingresa la cantidad de Millas a convertir: '))
        resultado = round(convertir*miles_to_km, 2)
        print(f'{convertir} millas son {resultado} Kms')
    else:
        print("⚠ Elegiste una opcion incorrecta")


if __name__ == "__main__":
    run()
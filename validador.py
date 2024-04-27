def validate(opciones, eleccion):
    # Definir validación de eleccion
    while eleccion not in opciones:
        print("Opcion no valida, ingrese una de las opciones validas: " , opciones)
        eleccion = input('Ingrese una opción valida: ')
    ##########################################################################
    ##########################################################################
    return eleccion


if __name__ == '__main__':
    numeros = ['0', '1', '2', '3']  # Ejemplo de conjunto de opciones
    eleccion = input('Ingrese una opción: ')
    eleccion_validada = validate(numeros, eleccion)
    print('La opción ingresada es:', eleccion_validada)
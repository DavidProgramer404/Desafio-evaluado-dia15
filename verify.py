import preguntas as p


def verificar(alternativas, eleccion):
    # Convertir la elección del usuario a un índice (A: 0, B: 1, C: 2, D: 3)
    indice_eleccion = ord(eleccion.lower()) - ord('a')

    # generar lógica para determinar respuestas correctas
    alternativas_correctas = [i for i, (_, correcta) in enumerate(alternativas) if correcta == 1]
    ##########################################################################################

    # Verificar si la elección del usuario coincide con alguna de las alternativas correctas
    correcto = indice_eleccion in alternativas_correctas
    
    if correcto:
        print('Respuesta Correcta')
    else:
        print('Respuesta Incorrecta')
    
    return correcto



if __name__ == '__main__':
    from print_preguntas import print_pregunta
    
    # Siempre que se escoja la alternativa con alt_2 estará correcta, e incorrecta en cualquier otro caso
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print_pregunta(pregunta['enunciado'],pregunta['alternativas'])
    respuesta = input('Escoja la alternativa correcta:\n> ').lower()
    verificar(pregunta['alternativas'], respuesta)

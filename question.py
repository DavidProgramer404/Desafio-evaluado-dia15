import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
opciones = {'basicas': [1, 2, 3],
            'intermedias': [1, 2, 3],
            'avanzadas': [1, 2, 3]}

def choose_q(dificultad):
    # Escoger preguntas por dificultad
    preguntas_disponibles = p.pool_preguntas[dificultad]
    
    # Obtener las preguntas disponibles
    preguntas = list(preguntas_disponibles.keys())
    
    # Escoger una pregunta aleatoria
    pregunta_elegida = random.choice(preguntas)
    
    # Obtener el enunciado y las alternativas de la pregunta elegida
    enunciado = preguntas_disponibles[pregunta_elegida]['enunciado']
    alternativas = shuffle_alt(preguntas_disponibles[pregunta_elegida])
    
    return enunciado, alternativas

if __name__ == '__main__':
    # Prueba básica para verificar que la función devuelve una pregunta y alternativas
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')

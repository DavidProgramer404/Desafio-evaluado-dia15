import preguntas as p
import random

def shuffle_alt(pregunta):
    # Mezclar alternativas
    alternativas = pregunta['alternativas']
    random.shuffle(alternativas)
    return alternativas

if __name__ == '__main__':
    # Si se ejecuta el programa varias veces, las alternativas deberían aparecer en distinto orden
    pregunta = p.pool_preguntas['basicas']['pregunta_2']
    print(shuffle_alt(pregunta)) 
    # A modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]

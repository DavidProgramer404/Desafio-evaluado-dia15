# No modificar
from verify import verificar
import preguntas as p
from question import choose_q
from print_preguntas import print_pregunta
from level import choose_level
from validador import validate
import time
import os
import sys

# valores iniciales - 
n_pregunta = 0
continuar = 'y'
correcto = True
p_level = 10
op_sys = 'cls' if sys.platform == 'win32' else 'clear'


# ----------------------------------------

os.system(op_sys) # limpiar pantalla

print('Bienvenido a la Trivia')
opcion = input('''Ingrese una opción para Jugar!
        1. Jugar
        0. Salir
        
    > ''')
# 1. validar opcion
opcion = validate(['0','1'], opcion)

# 2. Definir el comportamiento de Salir
if opcion == '0':
    print('Nos vemos pronto')
    time.sleep(2)
    os.system(op_sys)
    # finalizar programa
    sys.exit()

# Funcionamiento de preguntas
while correcto and n_pregunta < 3 * int(p_level):
    if n_pregunta == 0:
        p_level = input('¿Cuántas preguntas por nivel? (Máximo 3): ')
        # Validar el número de preguntas por nivel
        p_level = validate(['1', '2', '3'], p_level)
        
    if continuar == 'y':
        #contador de preguntas
        n_pregunta += 1
        # 4. Escoger el nivel de la pregunta
        nivel = choose_level(n_pregunta, p_level)  # No es necesario convertir p_level a int aquí
        print(f'Pregunta {n_pregunta} Nivel {nivel}:')
        # 5. Escoger el enunciado y las alternativas de una pregunta según el nivel escogido
        enunciado, alternativas = choose_q(nivel)
        #6. Imprimir el enunciado y sus alternativas en pantalla
        print_pregunta(enunciado, alternativas)
        
        respuesta = input('Escoja la alternativa correcta:\n> ').lower()
        # 7. Validar la respuesta entregada
        respuesta = validate(['a', 'b', 'c', 'd'], respuesta)
        # 8. Verificar si la respuesta es correcta o no
        correcto = verificar(alternativas, respuesta)
        
        if correcto and n_pregunta < 3 * int(p_level):
            print('Respuesta correcta. ¡Sigue así!')
            continuar = input('¿Desea continuar? [y/n]: ').lower()
            # Validar si es que se responde y o n
            continuar = validate(['y', 'n'], continuar)
            os.system(op_sys)
        elif correcto and n_pregunta == 3 * int(p_level):
            print(f'Felicitaciones, has respondido {3*int(p_level)} preguntas correctas.')
            print('¡Has ganado la Trivia!')
            print('Gracias por jugar, ¡hasta luego!')
            time.sleep(3)
            os.system(op_sys)
            sys.exit()
        else:
            print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas.')
            print('¡Sigue participando!')
            time.sleep(3)
            sys.exit()
    else:
        print('Nos vemos la próxima vez, sigue practicando')
        time.sleep(3)
        sys.exit()

print("valor de nivel", nivel)
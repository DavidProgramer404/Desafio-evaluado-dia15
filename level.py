def choose_level(n_pregunta, p_level):
    # Construir lógica para escoger el nivel
    # Validar el nivel de experiencia para el nivel de dificultad.
    if p_level == 1:
        level = "básicas"
    elif p_level == 2:
        level = "intermedias"  # Corregido para incluir p_level == 2 en "intermedias"
    else:
        level = "avanzadas"
    
    return level

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # intermedias
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # avanzadas

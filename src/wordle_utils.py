from datetime import datetime


def es_palabra_valida(cadena: str) -> bool:
    '''
    Comprueba si la cadena es una palabra válida:
    - Tiene 5 letras
    - Solo contiene letras a-z o A-Z

    Parámetros:
        cadena: la cadena a comprobar
    Devuelve:
        True si la cadena es una palabra válida, False en otro caso
    '''
    if len(cadena) != 5:
        return False

    for letra in cadena:
        if not ("a" <= letra <= "z" or "A" <= letra <= "Z"):
            return False

    return True
    


def calcula_minutos_y_segundos(inicio: datetime, fin: datetime) -> tuple:
    """ 
    Recibe dos datetime y devuelve la diferencia en minutos y segundos.
    
    Parámetros:
        inicio: datetime de inicio
        fin: datetime de fin
    Devuelve:
        Una tupla (minutos, segundos) con la diferencia entre los dos datetime
    """
    tiempo = fin - inicio
    segundos_totales = int(tiempo.total_seconds())

    minutos = segundos_totales // 60
    segundos = segundos_totales % 60

    return minutos, segundos

    
    

# TODO: Escribe la cabecera completa e implementa la función quitar_letra

def quitar_letra(texto: str, caracter: str) -> str:
    resultado = ""
    eliminada = True
    for letra in palabra:
        if letra == caracter and not eliminada:
            

    else:
        print(palabra)




#  TODO: Escribe la cabecera completa e implementa la función marcar_verdes

def marcar_verdes(palabra_secreta, intento_jugador):
     verdes =
     restantes =
     for letra i



# TODO: Escribe la cabecera completa e implementa la función marcar_amarillos

def obtener_pistas(palabra_secreta: str, intento: str) -> str:
    """
    Devuelve la cadena de pistas para un intento dado.
    Parámetros:
        palabra_secreta: la palabra secreta
        intento: la palabra del intento
    Devuelve:
        Una cadena de 5 caracteres con 'V', 'A' y '_'
    """


    # TODO: Implementa esta función
    return "_____"  # Elimina esta línea cuando la implementes



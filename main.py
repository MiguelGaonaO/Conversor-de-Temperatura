import conversor_de_escalas as cde

def determinar_conversor_escala(escala):
    """
    Elige qué función del módulo de conversor_de_escalas utilizar basada en la escala proporcionada.

    Parámetros:
    escala (str): La escala de temperatura original (Celsius, Fahrenheit, Kelvin).

    Retorna:
    function: La función correspondiente para la conversión de temperatura.
    """
    conversores = {
        'celsius': cde.celsius,
        'kelvin': cde.kelvin,
        'fahrenheit': cde.fahrenheit
    }
    return conversores.get(escala.lower())

def obtener_entrada_usuario():
    """Obtiene y valida la entrada del usuario para temperatura y escalas."""
    try:
        temperatura = float(input("Dime la temperatura: "))
    except ValueError:
        print("Error: La temperatura debe ser un número.")
        return None, None, None

    escala_origen = input("Dime la escala de temperatura (Celsius, Fahrenheit o Kelvin): ").lower()
    escala_destino = input("Dime a qué escala de temperatura lo vas a pasar: ").lower()
    
    if escala_origen not in ['celsius', 'fahrenheit', 'kelvin'] or escala_destino not in ['celsius', 'fahrenheit', 'kelvin']:
        print("Error: Escalas de temperatura no válidas.")
        return None, None, None

    return temperatura, escala_origen, escala_destino

def main():
    """Pide la información para convertir la temperatura y muestra el resultado"""

    # Pide al usuario la temperatura a convertir, su respectiva escala y a qué escala desea la conversión
    print("Bienvenido al conversor de temperatura.")

    temperatura, escala_origen, escala_destino = obtener_entrada_usuario()
    
    if temperatura is None:
        return  # Salir si hubo un error en la entrada

    funcion_conversor = determinar_conversor_escala(escala_origen)

    if funcion_conversor is not None:
        conversion = funcion_conversor(temperatura, escala_destino)
        if conversion is not None:
            print(f"La temperatura {temperatura} en {escala_origen.capitalize()} a {escala_destino.capitalize()} es {conversion}")
        else:
            print(f"Error: No se pudo convertir de {escala_origen.capitalize()} a {escala_destino.capitalize()}.")
    else:
        print(f"Error: Escala de temperatura origen '{escala_origen.capitalize()}' no válida.")

if __name__ == "__main__":
    main()

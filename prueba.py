# Importa el módulo que convierte las escalas de temperatura
import conversor_de_escalas as cde

def determinar_conversor_escala(escala):
    """Elige qué función del módulo utilizar para la conversión de temperatura"""
    if escala == 'Celsius':
        return cde.celsius
    elif escala == 'Kelvin':
        return cde.kelvin
    elif escala == 'Fahrenheit':
        return cde.fahrenheit
    # Si no se cumplen las condiciones, retorna None
    return None

def main():
    """Pide la información para convertir la temperatura y muestra el resultado"""

    # Pide al usuario la temperatura a convertir, su respectiva escala y a qué escala desea la conversión
    print("Bienvenido al conversor de temperatura.")
    temperatura = float(input("Introduce la temperatura: "))
    escala_origen = input("Introduce la escala de temperatura (Celsius, Fahrenheit o Kelvin): ")
    escala_destino = input("Introduce la escala de temperatura a la que deseas convertir: ")
    
    # Determina qué función del módulo utilizar para la conversión
    funcion_conversor = determinar_conversor_escala(escala_origen)

    if funcion_conversor is not None:
        # Llama a la función del módulo y pasa los argumentos
        conversion = funcion_conversor(temperatura, escala_destino)
        if conversion is not None:
            # Muestra el resultado de la conversión
            print(f"La temperatura {temperatura} en {escala_origen} es {conversion} en {escala_destino}.")
        else:
            print("Error: Escala de temperatura destino no válida.")
    else:
        print("Error: Escala de temperatura origen no válida.")

if __name__ == "__main__":
    main()

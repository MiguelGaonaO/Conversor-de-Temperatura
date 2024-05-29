def celsius(temperatura, escala_destino):
    if escala_destino == 'Kelvin':
        return temperatura + 273.15
    elif escala_destino == 'Fahrenheit':
        return temperatura * (9 / 5) + 32


def kelvin(temperatura, escala_destino):
    if escala_destino == 'Celsius':
        return temperatura - 273.15
    elif escala_destino == 'Fahrenheit':
        return (temperatura - 273.15) * (9 / 5) + 32


def fahrenheit(temperatura, escala_destino):
    if escala_destino == 'Celsius':
        return (temperatura - 32) * (5 / 9)
    elif escala_destino == 'Kelvin':
        return (temperatura - 32) * (5 / 9) + 273.15
import conversor_de_escalas as cde

def test_celsius_a_kelvin():
    resultado = cde.celsius(40, 'Kelvin')
    assert resultado == 313.15

def test_celsius_a_fahrenheit():
    resultado = cde.celsius(40, 'Fahrenheit')
    assert resultado == 104.0

def test_kelvin_a_celsius():
    resultado = cde.kelvin(313.15, 'Celsius')
    assert resultado == 40.0

def test_kelvin_a_fahrenheit():
    resultado = cde.kelvin(313.15, 'Fahrenheit')
    assert resultado == 104.0

def test_fahrenheit_a_celsius():
    resultado = cde.fahrenheit(104.0, 'Celsius')
    assert resultado == 40.0

def test_fahrenheit_a_kelvin():
    resultado = cde.fahrenheit(104.0, 'Kelvin')
    assert resultado == 313.15

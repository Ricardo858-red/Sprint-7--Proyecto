
# CODIGOS DE PRUEBA

# Un pytest busca en el codigo funciones con nombres que comiencen con test_
# y ejecuta eesas funciones al encontrarlas, si no genera un AssertionException



# Crea la función sign()
def sign(x):
    """Devuelve el signo de número."""
    if x == None:
        return None
    if x < 0:
        return -1
    return 1

# Prueba la función sign()
def test_sign():
    assert sign(-10) == -1
    assert sign(10) == 1
    assert sign(0) == 1
    assert sign(None) == None


def get_age_group(age):
    """
    Devuelve el grupo de edad basado en la edad en años dentro del intervalo 0..150
    de lo contrario, devuelve 'desconocido'.
    """
    if 0 <= age <= 14:
        return 'infancia'
    elif 15 <= age <= 24:
        return 'juventud'
    elif 25 <= age <= 64:
        return 'adulto'
    elif 65 <= age < 150:
        return 'vejez'
    else:
        return 'desconocido'


def test_get_age_group():
    """prueba unitaria para get_age_group"""
    assert get_age_group(-1) == 'desconocido'
    assert get_age_group(0) == 'infancia'
    assert get_age_group(14) == 'infancia'
    assert get_age_group(15) == 'juventud'
    assert get_age_group(24) == 'juventud'
    assert get_age_group(25) == 'adulto'
    assert get_age_group(64) == 'adulto'
    assert get_age_group(65) == 'vejez'
    assert get_age_group(80) == 'vejez'
    assert get_age_group(150) == 'desconocido'

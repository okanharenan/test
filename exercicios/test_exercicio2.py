from exercicio2 import valor


def test_valor():
    assert valor(100) == 9.00
    assert valor(101) == 11.00
    assert valor(201) == 4.00

def test_calculo():
    assert valor(100) + valor(100) == 18
    assert valor(101) + valor(100) == 20

from exercicio2 import valor


def test_valor():
    assert valor(100) == 9.00
    assert valor(101) == 11.00
    assert valor(201) == 4.00
from exercicio3 import calcular_preco_volume


def test_calcular_preco_volume():
    assert calcular_preco_volume(100) == 10.0
    assert calcular_preco_volume(9823) == 20.0
    assert calcular_preco_volume(29820) == 30.0
    assert calcular_preco_volume(99999) == 20.0
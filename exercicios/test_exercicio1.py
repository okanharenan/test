from exercicio1 import desconto


def test_desconto_10_99():
    assert desconto(10, 30) == (285.0, 300.0)

def test_desconto_100_999():
    assert desconto(10, 200) == (1800, 2000)

def test_desconto_acima_1000():
    assert desconto(10, 12000) == (102000, 120000)

def test_sem_desconto():
    assert desconto(10, 5) ==  (50, 50)
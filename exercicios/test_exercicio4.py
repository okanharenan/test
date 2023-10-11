from exercicio4 import *


def test_code():
    assert gerar_codigo() == 1
    assert cadastrar_peca() == 1

    peca = {
        'codigo': 100,
        'nome': 'peca',
        'fabricante': 'fabricante',
        'valor': 200
    }
    assert imprimir_peca(peca) == '100 fabricante 200.00'
# -*- coding: utf-8 -*-


def calcula_valor(preco_litro: float, litros: float, tipo: str) -> float:
    """
    Calcula o valor a ser pago de acordo com o tipo de combustível, a quantidade de litros
    e o preço
    """
    if tipo == "a":
        preco_litro = preco_litro * 0.97 if litros <= 20 else preco_litro * 0.95
        return preco_litro * litros

    if tipo == "g":
        preco_litro = preco_litro * 0.96 if litros <= 20 else preco_litro * 0.94
        return preco_litro * litros

    raise KeyError

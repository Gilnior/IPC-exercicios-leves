# -*- coding: utf-8 -*-

def pagamento(atual: float)->float:
    """
    Função que recebe o salários atual e retorna seu valor ajustado com base
    na tabela disponibilizada
    """
    reajuste = 1.2 if atual <= 280 else 1.15 if atual <= 700 else 1.1 if atual <= 1500 else 1.05
    reajustado = atual * reajuste

    return reajustado

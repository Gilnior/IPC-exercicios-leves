# -*- coding: utf-8 -*-


def verifica_triangulo(x, y, z) -> bool:
    """
    Verifica se os 3 lados podem formar um triângulo retornando True ou False
    """
    if (x < z + y) and (z < x + y) and (y < x + z):
        return True
    return False


def tipo_triangulo(x, y, z) -> str:
    """
    Retorna o tipo de triângulo que poderia ser formado com os lados fornecidos
    """
    if verifica_triangulo(x, y, z):
        tipo = (
            "Equilátero"
            if x == y == z
            else "Isósceles"
            if x == y or y == z or z == x
            else "Escaleno"
        )
        return tipo

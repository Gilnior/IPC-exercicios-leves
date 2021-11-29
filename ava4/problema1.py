# -*- coding: utf-8 -*-

def soma_divisores(num: int)-> int:
    divisores = [a for a in range(1, num + 1) if num % a == 0 and a != num]
    if 1 not in divisores: divisores.insert(0, 1)
    return sum(divisores)
    
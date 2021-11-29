# -*- coding: utf-8 -*-

x = int(input("Digite o valor de x: ")) # 1
y = int(input("Digite o valor de y: ")) # 20

quadrados = [n for n in range(x, y + 1) if (n**(1/2)).is_integer()]

[print(n) for n in quadrados]

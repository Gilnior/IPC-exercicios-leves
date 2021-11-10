# -*- coding: utf-8 -*-

a = float(input("Digite o valor de a: ")) # 2
b = float(input("Digite o valor de b: ")) # 5
c = float(input("Digite o valor de c: ")) # 8

if a != 0:
    delta = b**2 - 4*a*c
    _ = (
        print("Não existe raiz real") if delta < 0 else print("Raiz única") if delta == 0 else None
        )

    if delta >= 0:
        x1, x2 = (-b+delta**(1/2))/(2*a), (-b-delta**(1/2))/(2*a)
        _ = print(f"Raiz = {x1:.2f}") if x1 == x2 else print(f"Raiz1 = {x1:.2f}\nRaiz2 = {x2:.2f}")

else:
    print("Não é uma equação quadrática")

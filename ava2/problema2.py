# -*- coding: utf-8 -*-

x = float(input("Digite o comprimento do primeiro lado:"))  # 1
y = float(input("Digite o comprimento do segundo lado:"))  # 2
z = float(input("Digite o comprimento do terceiro lado:"))  # 5

TRIANGULOS = {
    "escaleno": "Triângulo Escaleno",
    "isosceles": "Triângulo Isósceles",
    "equilatero": "Triângulo Equilátero",
}

if (x < z + y) and (z < x + y) and (y < x + z):
    if x == y == z:
        print(TRIANGULOS["equilatero"])
    elif x == y or y == z or z == x:
        print(TRIANGULOS["isosceles"])
    else:
        print(TRIANGULOS["escaleno"])

else:
    print("Não é um triângulo")

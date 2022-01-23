# -*- coding: utf-8 -*-

def mdc(x, y):
    if y == 0:
        return x
    else:
        return mdc(y, x%y)

x = int(input("Digite x: "))  # 16
y = int(input("Digite y: "))  # 36

print(mdc(x, y))  # 4
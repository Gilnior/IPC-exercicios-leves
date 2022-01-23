# -*- coding: utf-8 -*-

def power(k, n):
    if n == 1:
        return k
    else:
        return k * power(k, n - 1)


k = int(input("Digite k: "))  # 2
n = int(input("Digite n: "))  # 3

print(power(k, n))
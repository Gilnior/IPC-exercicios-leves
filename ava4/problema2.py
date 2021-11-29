# -*- coding: utf-8 -*-

n = int(input("Digite n: "))

h = [1/x for x in range(1, n + 1)]

print("Resultado: {:.2f}".format(sum(h)))
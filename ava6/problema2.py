# -*- coding: utf-8 -*-

a = [int(input()) for i in range(10)]

mean = sum(a)/len(a)

sd = (sum([(n-mean)**2 for n in a])/9)**(1/2)

print("Desvio Padrão: {:.2f}".format(sd))

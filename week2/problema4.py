# -*- coding: utf-8 -*-

sal = float(input("Digite o valor do salário: "))

res = "Valor do aumento: {:.2f}\nNovo salário: {:.2f}"

if not sal > 280:
    print(res.format(sal*20/100, sal*1.2))
elif not sal > 700:
    print(res.format(sal*15/100, sal*1.15))
elif not sal > 1500:
    print(res.format(sal*10/100, sal*1.1))
else:
    print(res.format(sal*5/100, sal*1.05))

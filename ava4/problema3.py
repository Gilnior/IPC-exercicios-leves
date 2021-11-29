# -*- coding: utf-8 -*-

sal_carlos = float(input("Digite o salário do Carlos: ")) # 2000
sal_joao = sal_carlos/3
rend_poupanca = float(input("Digite o rendimento da poupança(%): "))/100 # 2, para Carlos
renda_fixa = float(input("Digite o rendimento do fundo de renda fixa(%): "))/100 # 5, para João

calc_juros = lambda n, i: n * (1 + i)

t = 0
while sal_joao < sal_carlos:
    sal_carlos = calc_juros(sal_carlos, rend_poupanca)
    sal_joao =  calc_juros(sal_joao, renda_fixa)
    t += 1

print(f"Meses: {t}") # 38

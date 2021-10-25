"""
Escreva um programa que solicita ao usuário um valor de velocidade (v0 ), um valor de aceleração (a) e
um valor de tempo (t ) e o programa imprime na tela a velocidade final e a distância percorrida por um
veículo após o intervalo de tempo t , com velocidade inicial igual a v0 e aceleração igual a a
"""
V0 = float(input("Digite o valor da velocidade: "))
A = float(input("Digite o valor da aceleração: "))
T = float(input("Digite o valor do tempo: "))

RESPOSTA = "Velocidade final: {V:.2f}\nDistância percorrida: {S:.2f}"
RESPOSTAS = {"V": V0+A*T, "S": V0*T + A*(T**2)/2}
RESPOSTAS = {k: round(v, 2) for k,v in RESPOSTAS.items()}

print(RESPOSTA.format_map(RESPOSTAS))

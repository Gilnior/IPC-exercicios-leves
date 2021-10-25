"""
Escreva um programa que solicita ao usuário um intervalo de tempo em segundos e o programa im-
prime na tela o valor correspondente em horas, minutos e segundos
"""
TEMPO = int(input("Digite o valor do tempo em segundos: "))

RESPOSTA = "Valor convertido: {h} h {m} min {s} s"

horas = TEMPO//(60*60)
minutos = (TEMPO%(60*60))//60
segundos = TEMPO%60

RESPOSTAS = {"h": horas, "m": minutos, "s": segundos}

print(RESPOSTA.format_map(RESPOSTAS))

# -*- coding: utf-8 -*-

money_hour = float(input("Digite o valor da hora de trabalho: "))  # 16.0
hours = float(input("Digite a quantidade de horas trabalhadas no mês: "))  # 160

money = money_hour * hours

irpf = money * (
    0 if money <= 900 else 0.05 if money <= 1500 else 0.1 if money <= 2500 else 0.2
)
inss = money * 0.1
fgts = money * 0.11
descontos = sum([irpf, inss])
formated_value = [
    f"R$ {value:.2f}"
    for value in [money, irpf, inss, fgts, descontos, money - descontos]
]

print("Salário Bruto:", formated_value[0])  # R$ 2560.00
print("IR:", formated_value[1])  # R$ 512.00
print("INSS:", formated_value[2])  # R$ 256.00
print("FGTS:", formated_value[3])  # R$ 281.60
print("Total de descontos:", formated_value[4])  # R$ 768.00
print("Salário líquido:", formated_value[5])  # R$ 1792.00

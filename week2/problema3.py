# -*- coding: utf-8 -*-

idade = int(input("Digite a idade: "))  # 60
tempo_contribuicao = int(input("Digite o tempo de contribuição: "))  # 35
sexo = input("Digite o sexo (M/F): ").strip()  # M

RESULTADO = (
    "Pode aposentar"
    if (sexo == "M" and ((idade >= 65) or (idade >= 60 and tempo_contribuicao >= 35)))
    or (sexo == "F" and ((idade >= 60) or (idade >= 55 and tempo_contribuicao > 30)))
    else "Não pode aposentar"
)

print(RESULTADO)

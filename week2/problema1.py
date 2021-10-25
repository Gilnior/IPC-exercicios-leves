"""
Faça um programa que leia cinco números inteiros e identifique:
• O maior valor informado
• O menor valor informado
• Quantos números são divisíveis por 3
"""

val = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]
inteiros = sorted([int(input(f"Digite o {i} inteiro: ")) for i in val])

RESPOSTA = "Maior: {maior}\nMenor: {menor}\nQuantidade de divisíveis por 3: {divisiveis_3}"

print(RESPOSTA.format_map(
    {"maior": inteiros[-1],
    "menor": inteiros[0],
    "divisiveis_3": len([i for i in inteiros if i % 3 == 0])
    }))

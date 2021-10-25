"""
Faça um programa que leia cinco números inteiros e identifique:
• O maior valor informado
• O menor valor informado
• Quantos números são divisíveis por 3
"""

# n1 = int(input("Digite o primeiro inteiro: "))
# n2 = int(input("Digite o segundo inteiro: "))
# n3 = int(input("Digite o terceiro inteiro: "))
# n4 = int(input("Digite o quarto inteiro: "))
# n5 = int(input("Digite o quinto inteiro: "))

val = ["primeiro", "segundo", "terceiro", "quarto", "quinto"]
inteiros = sorted([int(input(f"Digite o {i} inteiro: ")) for i in val])

RESPOSTA = (
    "Maior: {maior}\nMenor: {menor}\nQuantidade de divisíveis por 3: {divisiveis_3}"
)

print(
    RESPOSTA.format_map(
        {
            "maior": inteiros[-1],
            "menor": inteiros[0],
            "divisiveis_3": len([i for i in inteiros if i % 3 == 0]),
        }
    )
)

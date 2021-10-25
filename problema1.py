"""
Escreva um programa que solicita ao usuário o raio de uma circunferência e o programa imprime na
tela o valor do perímetro e da área dessa circunferência, além do volume da esfera formada por essa
circunferência.
"""
PI = 3.1415
r = raio = float(input("Digite o valor do raio da circunferência:"))

RESPOSTA = "Perímetro:{perimetro}\n"
RESPOSTA += "Área:{area}\n"
RESPOSTA += "Volume:{volume}"

RESPOSTAS = {"perimetro": 2*PI*r, "area": PI*(r**2), "volume": 4*PI*(r**3)/3}
RESPOSTAS = {k: round(v, 2) for k,v in RESPOSTAS.items()}

print(RESPOSTA.format_map(RESPOSTAS))

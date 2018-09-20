import math

x1 = int(input("Digite o valor de x1: "))
x2 = int(input("Digite o valor de x2: "))
y1 = int(input("Digite o valor de y1: "))
y2 = int(input("Digite o valor de y2: "))

d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print("Distância entre P1 e P2 é: ", d)

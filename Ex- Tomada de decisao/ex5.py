print("Digite os 3 comprimentos dos lados do triângulo")

lado1 = int(input())
lado2 = int(input())
lado3 = int(input())

if (lado1 == lado2 == lado3):
    print("Equilátero")
elif (lado1 != lado2 != lado3):
    print("Escaleno")
else:
    print("Isóceles")
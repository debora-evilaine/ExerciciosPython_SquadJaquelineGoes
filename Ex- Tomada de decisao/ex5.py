
lado1, lado2, lado3 = [int(lado1) for lado1 in input("Entre com os 3 lados do triângulo separados por espaço: ").split()]

if lado1 == lado2 == lado3:
    print("O triângulo é equilátero!")

elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("O triângulo é isóceles!")

else:
    print("O triângulo é escaleno!")

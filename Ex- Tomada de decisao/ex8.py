
numero1, numero2, numero3 = [int(numero1) for numero1 in input("Entre com 3 números separados por espaços: ").split()]

maior = numero1

if numero2 > maior:
    maior = numero2

if numero3 > maior:
    maior = numero3

print(f"O número maior entre {numero1}, {numero2} e {numero3} é: ", maior)
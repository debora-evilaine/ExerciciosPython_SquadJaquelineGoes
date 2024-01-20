"""
Façaumprogramaquelêtrêsnúmerosinteiroseosmostraemordemcrescente.

"""

numero1, numero2, numero3 = [int(numero1) for numero1 in input("Entre com 3 números separados por espaço: ").split()]

maior = numero1

if numero2 > maior:
    maior = numero2
    menor = numero1
    meio = numero1

else:
    menor = numero2
    meio = numero2

if numero3 > maior:
    if maior > menor:
        meio = maior
        maior = numero3

    else:
        menor = maior
        maior = numero3

else:
    if numero3 > menor:
        meio = numero3

print(menor, meio, maior)
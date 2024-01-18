"""
Cálculo do IMC
"""

peso = float(input("Informe o seu peso: "))

altura = float(input("Informe a sua altura: "))

imc = peso / (altura ** 2)

print("Com base no seu peso e altura, o seu imc é: ", imc)
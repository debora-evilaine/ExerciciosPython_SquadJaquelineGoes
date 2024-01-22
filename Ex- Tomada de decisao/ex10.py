# Solicitar três números inteiros ao usuário
numero1 = int(input("Digite o primeiro número inteiro:  "))
numero2 = int(input("Digite o segundo número inteiro:  "))
numero3 = int(input("Digite o terceiro número inteiro:  "))

# Colocar os números em uma lista e ordená-los
numeros = [numero1, numero2, numero3]
numeros.sort()

# Exibir os números em ordem crescente
print("Números em ordem crescente:", numeros)

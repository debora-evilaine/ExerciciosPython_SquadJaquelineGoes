# Inicializar contadores
pares = 0
impares = 0

while True:
    # Solicitar um número ao usuário
    numero = int(input("Digite um número positivo (ou 0 para encerrar):  "))

    # Validar se o número é positivo
    if numero < 0:
        print("Número inválido. Digite um número positivo. ")
        continue
    
    # Verificar se o número é zero (para encerrar)
    if numero == 0:
        break

    # Contar números pares e ímpares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Exibir o resultado
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
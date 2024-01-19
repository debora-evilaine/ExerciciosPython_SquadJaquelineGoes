pares = 0
impares = 0

while True:
    numeros = int(input("Entre com os números positivos (0 para sair do loop): "))

    if numeros == 0:
        break

    if numeros < 0:
        continue

    if numeros % 2 == 0:
        pares += 1

    else:
        impares += 1

print(f"Quantidade de pares: {pares}\nQuantidade de ímpares: {impares}")
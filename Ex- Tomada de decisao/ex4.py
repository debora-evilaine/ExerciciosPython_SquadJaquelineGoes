
nota = int(input("Entre com uma nota de 0 a 10: "))

while nota not in range(0, 11):
    nota = int(input("Entre com uma nota de 0 a 10: "))

if nota >= 7:
    print("Você foi aprovado! :)")

else:
    print("Você foi reprovado! :(")
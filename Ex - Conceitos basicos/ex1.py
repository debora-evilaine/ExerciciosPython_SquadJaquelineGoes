"""
Peça dois números e realize as principais operações.
"""
# #SOMA
num1, num2 = (input("Entre com dois números separados por espaço: ").split())
# O split é utilizado para separar os números, que são recebidos como uma única string, 
# em duas strings.

num1 = int(num1) # Agora, transformamos essas duas strings em ints e associamos às 
                 # variáveis corretas.
num2 = int(num2)

print(f"A soma de {num1} com {num2} é: ", num1 + num2)

#SUBTRAÇÃO
numero1, numero2 = [int (numero1) for numero1 in input("Entre com dois números separados por espaço: ").split()]
# Esta abordagem usa a lista comprehension para: pegar o input do usuário e fazer o split em duas strings
# e logo depois transformar essas duas strings em inteiros, tudo em uma linha só

print(f"A subtração de {numero1} e {numero2} é: ", numero1 - numero2)

"""
Peça dois números e realize as principais operações.
"""
#SOMA
num1, num2 = (input("Entre com dois números separados por espaço: ").split())
# O split é utilizado para separar os números, que são recebidos como uma única string, 
# em duas strings.

num1 = int(num1) # Agora, transformamos essas duas strings em ints e associamos às 
                 # variáveis corretas.
num2 = int(num2)

print(f"A soma de {num1} com {num2} é: ", num1 + num2)
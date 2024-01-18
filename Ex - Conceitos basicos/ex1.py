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

#=====================================================

# SUBTRAÇÃO
numero1, numero2 = [int (numero1) for numero1 in input("Entre com dois números separados por espaço: ").split()]
# Esta abordagem usa a lista comprehension para: pegar o input do usuário e fazer o split em duas strings
# e logo depois transformar essas duas strings em inteiros, tudo em uma linha só

print(f"A subtração de {numero1} e {numero2} é: ", numero1 - numero2)

#=====================================================

# MULTIPLICAÇÃO 

n1, n2 = [int(n1) for n1 in input("Entre com dois números separados por espaço: ").split()]

# A lista comprehension será usada para o restante das operações
print(f"A multipliação de {n1} com {n2} é: ", n1 * n2)

#=====================================================

# DIVISÃO

nu1, nu2 = [int(nu1) for nu1 in input("Entre com dois números separados por vírgula, sem espaços entre elas: ").split(",")]
# A divisão utiliza as vírgulas para separar as strings, ao invés do espaço utilizado anteriormente
print(f"A divisão de {nu1} por {nu2} é: ", nu1/nu2)
nota = int(input("Entre com uma nota entre 0 e 10: "))

while nota not in range(0, 11): # A função range exclui o último valor, por isso colocamos 
                                # até o 11 para que o 10 seja incluído
    nota = int(input("Entre com uma nota entre 0 e 10: "))

print("Yay!")
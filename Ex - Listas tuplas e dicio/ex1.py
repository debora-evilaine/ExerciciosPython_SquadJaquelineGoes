# Contagem das respostas afirmativas
respostas_afirmativas = 0

# Perguntas sobre o crime
pergunta1 = input("Telefonou para a vítima? (Sim/Não): ")
if pergunta1.lower() == "sim":
    respostas_afirmativas += 1

pergunta2 = input("Esteve no local do crime? (Sim/Não): ")
if pergunta2.lower() == "sim":
    respostas_afirmativas += 1

pergunta3 = input("Mora perto da vítima? (Sim/Não): ")
if pergunta3.lower() == "sim":
    respostas_afirmativas += 1

pergunta4 = input("Devia para a vítima? (Sim/Não): ")
if pergunta4.lower() == "sim":
    respostas_afirmativas += 1

pergunta5 = input("Já trabalhou com a vítima? (Sim/Não): ")
if pergunta5.lower() == "sim":
    respostas_afirmativas += 1

# Classificação da participação com base nas respostas
if respostas_afirmativas == 2:
    print("Suspeita: A pessoa deve ser investigada mais a fundo.")
elif 3 <= respostas_afirmativas <= 4:
    print("Cúmplice: A pessoa pode ter alguma participação no crime.")
elif respostas_afirmativas == 5:
    print("Assassino: A pessoa pode ser a principal suspeita.")
else:
    print("Inocente: A pessoa não parece ter envolvimento no crime.")
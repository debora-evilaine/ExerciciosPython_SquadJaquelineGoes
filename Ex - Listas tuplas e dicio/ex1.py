"""ExercíciosTuplas,ListaseDicionários1.
Utilizandolistasfaçaumprogramaquefaça5perguntasparaumapessoasobreumcrime.
Asperguntassão:Telefonouparaavítima?
Estevenolocaldocrime?Morapertodavítima?Deviaparaavítima?
Játrabalhoucomavítima?
Oprogramadevenofinalemitirumaclassificaçãosobreaparticipaçãodapessoanocrime.
Seapessoaresponderpositivamentea2questõeseladeveserclassificadacomo""Suspeita"",
entre3e4como""Cúmplice""e5como""Assassino"".Casocontrário,eleseráclassificadocomo""
Inocente"""

print("Atenção: Todas as respostas devem ser somente 's' ou 'n'")

respostas = []

pergunta = input("Telefonou para a vítima? ")

respostas.append(pergunta)

pergunta = input("Esteve no local do crime? ")

respostas.append(pergunta)


pergunta = input("Mora perto da vítima? ")

respostas.append(pergunta)


pergunta = input("Devia para a vítima? ")

respostas.append(pergunta)


pergunta = input("Já trabalhou com a vítima? ")

respostas.append(pergunta)

resposta_positiva = respostas.count('s')

if resposta_positiva == 2:
    print("Você é um suspeito! >:(")

elif resposta_positiva > 2 and resposta_positiva <= 4:
    print("Você é um cúmplice!")

elif resposta_positiva == 5:
    print("Você é um assassino, e está preso! >:(")

else:
    print("Você é inocente! :)")
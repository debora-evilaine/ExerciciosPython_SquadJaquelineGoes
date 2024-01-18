from datetime import datetime

"""
Peça o ano de nascimento e imprima a idade atual.
"""

data_de_nascimento = input("Entre com a sua data de nascimento no formato dd/mm/aaaa: ")

# A data inserida no input foi recebida como string, por isso utilizamos strptime para 
# transformar essa string em data
data_convertida = datetime.strptime(data_de_nascimento, "%d/%m/%Y")

# Pegamos a data atual como string
data_atual = datetime.now().strftime("%d%m%Y")

# Transformamos essa string em um objeto de data
data_atual_convertida = datetime.strptime(data_atual, "%d%m%Y")

# Agora fazemos os devidos cálculos para transformar essa data em um número que corresponda aos anos de idade
idade_atual = (data_atual_convertida - data_convertida)/365
"""
O resultado de uma operação com datetimes é um timedelta, que está como dias vividos.
Porém nós sabemos que esses dias vividos correspondem ao mesmo número de anos vividos, por isso
podemos pegar idade_atual.days e interpretar como os anos da pessoa.

Por exemplo: a data 28/02/2005 retornaria 6898 dias, que dividido por 365 daria aproximadamente 18 dias.
Esse resultado seria em dias, no entanto sabemos que esse resultado também representa a idade dessa pessoa em anos, considerando
a data atual de 18/01/2024. 

"""
print(f"Você tem {idade_atual.days} anos!")
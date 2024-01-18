"""
pergunte quanto vc ganha por hora e horas trabalhadas no mes. motre o salario total do mes
"""

salario_por_hora = float(input("Entre com o valor que você recebe por hora: "))

horas_trabalhadas = float(input("Entre com o total de horas trabalhadas no mês: "))

salario_total = salario_por_hora * horas_trabalhadas

print("O seu salário do mês é: ", salario_total)
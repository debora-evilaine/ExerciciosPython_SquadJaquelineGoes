"""
Quantidade em km e transforme em metros, cm e milimetros
"""

km = float(input("Entre com os quilômetros a serem convertidos: "))


metros = km * 1000

centimetros = km * 100000

milimetros = km * 1000000


print(f"{km:.0f} quilômetros são iguais a {metros:.0f} metros, {centimetros:.0f} centimetros, e {milimetros:.0f} milímetros!")
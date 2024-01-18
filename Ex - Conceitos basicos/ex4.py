"""
receba litros de combustivel consumudos e a distancia percorrida. calcule o consumo medio em km/l
"""

combustivel = float(input("Entre com a quantidade de litros de combustível consumidos: "))

distancia_percorrida = float(input("Entre com a distância percorrida: "))

km_por_litro = distancia_percorrida/combustivel

print(f"Você rodou {km_por_litro} quilômetros com {combustivel} litros de combustivel.")
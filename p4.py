"""
Problema 4:
Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
pantalla la suma de todos los enteros desde 1 hasta N. La suma de los N primeros enteros positivos
puede ser calculada de la siguiente forma:

n(n+1)/2
"""

num=int(input("Ingrese el entero positivo N: "))
suma_num = num*(num+1)/(2)

print(f"La suma es: {suma_num}")

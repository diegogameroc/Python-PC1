"""
Problema 5:
Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows.
"""
num_shows=int(input("¿Cuántos shows musicales ha visto el ultimo año ? "))
if num_shows > 3:
    print(True)
else:
    print(False)
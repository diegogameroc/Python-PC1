"""
Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
lista. Su programa debe retornar otra lista sin los duplicados.
Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
Lista procesada: [1, 2, 3, 4,5]
"""

lista = [1, 1, 2, 3, 4, 4, 5, 1]


lista_sindupli = list(set(lista))

print("Lista orginal: ")
print(lista)
print("Lista sin duplicados: ")
print(lista_sindupli)
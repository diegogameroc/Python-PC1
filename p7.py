"""
Problema 7:
Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.
"""

num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))

print("MENU CALCULADORA")
print("1.SUMA")
print("2.RESTA")
print("3.MULTIPLICACION")

opcion=int((input("Ingrese una opcion: ")))
suma=num1+num2
resta=num1-num2
multi=num1*num2

if opcion==1:
    print(f"El resultado es {suma}")
elif opcion==2:
    print(f"El resultado es {resta}")
elif opcion==3:
    print(f"El resultado es {multi}")
else:
    print("Introducir una opcion valida")    

"""
Supongamos que estás en un país donde se acostumbra desayunar entre las 7:00 y las 8:00, almorzar
entre las 12:00 y las 13:00 y cenar entre las 18:00 y las 19:00.
Implemente un programa que solicite al usuario una hora y le indique si es la hora del desayuno, la
hora del almuerzo o la hora de la cena. Si no es hora de comer, no envíes nada.
Suponga que la entrada del usuario se formatea en formato de 24 horas como #:## o ##:##. Y
suponga que el rango de tiempo de cada comida es inclusivo. Por ejemplo, ya sean las 7:00, las 7:01,
las 7:59 o las 8:00, o en cualquier momento intermedio, es hora de desayunar.
Nota:
Recuerde que cuando solicitamos datos a través de un input este nos devuelve un str, quizás le sea
más fácil realizar la comparación convirtiendo los datos a float.
Ejemplo :
Dato ingresado: “7:30” se puede interpretar como 7.5
Para ello, podemos usar el siguiente método de cadena para facilitar la obtención del dato. Puede
revisar otros métodos de cadena en el siguiente link.
"""
time = input("Ingrese una hora porfavor en este formato #:## :")

hours,minutes = time.split(":")
horas_reloj= int(hours) + (int(minutes)/60)
##print(f"Son LAS {horas_reloj}")

if horas_reloj>=7 and horas_reloj<=8:
    print("Es hora de desayunar")
elif horas_reloj>=12 and horas_reloj<=13:
    print("Es hora de almorzar")
elif horas_reloj>=18 and horas_reloj<=19:
    print("Es hora de cenar")
else: 
     None

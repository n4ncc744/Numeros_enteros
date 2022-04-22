"""Programa N0. 7:
Verificar si dos numeros son diferentes"""

print("-----------------------------")
print("-----NÚMEROS DIFERENTES------")
print("-----------------------------")

#input
X = int(input("Digite el valor de X: "))
Y = int(input("Digite el valor de Y: "))

#processing
if X != Y:
    msj = "Son diferentes"
    print("Son diferentes")
else:
    msj = "Son iguales"
#espacios son identación: las lineas se ejecutan si las condiciones son o verdaderas, o falsas.

#output
print("los numeros " + msj)

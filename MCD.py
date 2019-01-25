import sys
global a
global b
a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=0
def MCD(a,b):
    resto=0
    while (b>0):
        resto=b
        b=a%b
        a=resto
    return a
print("El MCD de los numeros ingresados es: ", MCD(a,b))
    

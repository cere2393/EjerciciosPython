#Realice un programa que solicite al usuario dos números los sume y muestre el resultado de la suma en pantalla,
# luego que solicite al usuario ingresar un tercer número,
# el programa debe mostrar en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.


n1=int((input("ingrese valor 1:")))
n2=int ((input("ingrese valor 2:")))
s=n1+n2
print(s)
n3=int((input("ingrese valor 3:")))
m= s*n3
print (m)

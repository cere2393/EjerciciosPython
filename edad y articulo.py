#Realice un programa que ingrese la edad de una persona 
# y la cantidad de artículos comprados en una tienda.
#El programa debe mostrar en pantalla un valor booleano (True o False) 
# que indique si la persona es mayor de 18 años de edad y además compró más de 1 artículo.

a=int (input("ingrese su edad:"))
b= int(input("cuantos articulos compro:"))
c= (a>18 and b>1)
print (c)


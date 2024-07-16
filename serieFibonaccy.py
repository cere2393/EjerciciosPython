#Realice un programa que imprima los 50 primeros numeros de la sucesion de Fibonacci empezando en 0.
#La serie Fibonacci se compone por una sucesion de numeros en la que el siguiente siempre es la suma de los dos anteriores
# 0,1,1,2,3,5,8,13


n= 0
a= 1
c= 0

for c in range (50):
    print(n)
    s=n+a
    n=a
    a=s
    
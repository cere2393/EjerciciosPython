#Realice un programa que al ingresar una letra si es una vocal, muestre el mensaje “Es vocal”.
#Además debe verificar si se ingresó un string de más de un carácter (es decir más de una letra),
# en ese caso debe mostrar un mensaje que diga: Sólo debe ingresar una letra.”.


while True:
    a1=input ("ingrese un caracter")
    if len(a1)==1:
        break
    else:
        print ("solo una letra")
V=["A","a","E","e","I","i","O","o","U","u"]
if a1 in V:
    print(f"{a1} es una vocal")
else:
    print (f"{a1} no es vocal")         
    
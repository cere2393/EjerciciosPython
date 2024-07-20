#Realice un programa que reciba un valor ingresado en temperatura en escala Fahrenheit (debe permitir decimales)
# y lo convierta a su equivalente en grados Celsius, luego muestre el resultado. 
# La fórmula de conversión que se usa para este cálculo es: celsius = (5/9) * (fahrenheit - 32)

Fahrenheit= float(input("ingrese grados Fahrenheit"))

celsius= (Fahrenheit-32)*(5/9)
print (celsius)
# Palabra o frase palíndromo

cadena = input("Digite una frase: ")

# Primero quitamos los espacios en blanco de la cadena
cadena = cadena.replace(" ","")

#Segundo, invertimos la cadena
cadena2 = cadena[::-1]

print(f"La cadena invertida es: {cadena2}")

if cadena == cadena2:
    print("Es una frase palíndroma")
else:
    print("NO es una frase palíndroma")

# Carolina EM

import unicodedata

def normalizar(texto):
    # Minusculas
    texto = texto.lower()
    
    # Quitar acentos
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    
    # Quitar todo lo que no sea letra
    texto = "".join(c for c in texto if c.isalnum())
    
    return texto


def es_palindromo(frase):
    texto = normalizar(frase)
    return texto == texto[::-1]


frase = input("Ingresa una frase: ")

if es_palindromo(frase):
    print("True → Es un palíndromo")
else:
    print("False → No es un palíndromo")

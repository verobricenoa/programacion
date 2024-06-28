#Escriba un programa que permita al usuario codificar y decodificar con dos métodos: 
#1. Codificación César 
#2. Codificación por primos

palabra = ""
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
primos = []

def descifrar(palabra, clave): 
    texto = ""
    for caracter in palabra.lower():
        if caracter in letras:
            indice = letras.index(caracter)
            nuevo_indice = (indice + clave) % len(letras)
            texto += letras[nuevo_indice]
    print(texto)

def cifrar(palabra, clave):
    texto = ""
    for caracter in palabra.lower():
        if caracter in letras:
            indice = letras.index(caracter)
            nuevo_indice = (indice - clave) % len(letras)
            texto += letras[nuevo_indice]
    print(texto)

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def lista_primos(limite):
    global primos
    primos = []
    for numero in range(2, limite + 1):
        if es_primo(numero):
            primos.append(numero)
    return primos

def cifrar_primos(palabra): 
    global primos
    texto = ""
    for caracter in palabra.lower(): 
        if caracter in letras: 
            indice = letras.index(caracter)
            numero_primo = primos[indice] if indice < len(primos) else 1
            texto += str(numero_primo)
    print(texto)

def descifrar_primos(palabra):
    global primos
    texto = ""
    for digito in palabra: 
        if digito.isdigit(): 
            numero_primo = int(digito)
            if numero_primo in primos:
                indice = primos.index(numero_primo)
                texto += letras[indice].upper() if indice < len(letras) else ''
    print(texto)

while True: 
    opcion = int(input("MENU\n1.CODIFICACION POR METODO CESAR\n2.CODIFICACION POR PRIMOS\n3.STOP"))
    if opcion == 1: 
        palabra = str(input("Ingrese una palabra: "))
        clave = int(input("Ingrese una clave de cifrado: "))
        menu1 = input("ELIJA UNA OPCION\nA.Cifrar\nB.Descifrar")
        if menu1 == "A":
            cifrar(palabra, clave)
        elif menu1 == "B": 
            descifrar(palabra, clave)
        else: 
            print("Ingrese una opcion valida")
    elif opcion == 2: 
        limite = 27
        lista_primos(limite)
        menu2 = input("ELIJA UNA OPCION\na.Cifrar\nb.Descifrar")
        if menu2 == "a": 
            palabra = str(input("Ingrese una palabra: "))
            cifrar_primos(palabra)
        elif menu2 == "b": 
            numeros = str(input("Ingrese una cadena de digitos a descifrar: "))
            descifrar_primos(numeros)
        else: 
            print("Ingrese una opcion valida")
    elif opcion == 3: 
        break 
    else: 
        print("Ingrese una opcion valida")
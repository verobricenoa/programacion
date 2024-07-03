#Ejercicio 3. Codificación y Decodificación por números primos. 

#VARIABLES 
palabra=""
primos=[]

#FUNCIONES 
def es_primo (numero): 
    if numero <=1: 
        return False 
    for i in range (2, int(numero**0.5 + 1)): 
        if numero %i==0:
            return True

def lista_primos(limite):
    global primos 
    primos=[]
    for numero in range (2, limite+1):
        if es_primo(numero): 
            primos.append(numero)
            return primos 

def codificar_primos(palabra): 
    global primos 
    texto=""
    for caracter in palabra.lower(): 
        if caracter in letras: 
            indice=letras.index(caracter)
            numero_primo=primos[indice] if indice < len (primos else 1)
            texto += str(numero_primo)
            print(texto)

def decodificar_primos(palabra): 
    global primos 
    texto=""
    for digito in plabra.lower(): 
        if digito.isdigit():
            numero_primo=int(digito)
            if numero_primo in primos: 
                texto += letras[indice].upper() if indice < len(letras)
                print (texto)

#PROGRAMA PRINCIPAL 
print("MENU.\n1.Codificar un mensaje\n2.Decodificar un mensaje\n3.Contar frecuencia de letras en el mensaje codificado\n4.Salir")
opcion=int(input("Ingrese una opcion: "))

while True: 
    if opcion == 1: 
        palabra=str(input("ingrese una palabra a codificar: "))
        palabra=palabra.lower()
        limite=27
        lista_primos(limite)
        codificar_primos(palabra)
    elif opcion == 2:
        palabra=str(input("ingrese una palabra a decodificar: "))
        limite=27
        lista_primos(limite)
        decodificar_primos(palabra)
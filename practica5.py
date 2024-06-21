#Cifrado de Cesar:
#abcdefghijklmnñopqrstuvwxyz
#vwxyzabcdefghijklmnñopqrstu
#Recibir un numero entero para e cifrado. Encriptar mensajes. 
#1. Solicitar al usuario una clave de cifrado. 
#2. Cifrar, descifrar o detener.

print ("Bienvenido. Este programa utiliza el CIFRADO DE CESAR para encriptar mensajes")
letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
palabra = ""
clave = int(input("Ingrese la clave de cifrado: "))

while True: 
    if (clave>len(letras)) : 
        clave=clave-len(letras)
    else: 
        break 

while True: 
    opcion= input("MENU\n1.Cifrar\n2.Descifrar\n3.Stop")
    if opcion == "1": 
        palabra = ""
        texto = input("Palabra a cifrar: ")
        for cifrar in texto: 
            for cesar in range(len(letras)):
                if (cifrar==letras[cesar] or cifrar==letras[cesar].upper()):
                    palabra += letras[cesar-clave]
        print (palabra)
    elif opcion == "2":
            palabra = ""
            texto = input("Palabra a descifrar: ")
            for cifrar in texto: 
                for cesar in range(len(letras)): 
                    if (cifrar==letras[cesar-clave] or cifrar==letras[cesar-clave].upper()): 
                        palabra += letras[cesar] 
            print(palabra)
    elif opcion == "3" : 
        break 
    else : 
        print ("Ingrese una opcion valida")

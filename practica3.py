#PRACTICA 3
#Escribir un programa que solicite al usuario un conjunto de números primos y calcule la suma de los cuadrados 
#de estos. Tenga en cuenta: 
#1. Si el usuario ingresa un valor no númerico ignorar dicho valor, enviar un mensaje y permitir reintentos.
#2. Si el usuario ingresa un número no primo ignorar dicho valor, enviar un mensaje y permitir reintentos. 
#3. Si el usuario ingresa el string 'stop' detener la solicitud de números al usuario. 

numero = []
while True: 
    palabra = input("Ingrese un numero primo:")
    if (palabra.isnumeric()):
        if (int(palabra)>0):
            palabra = int(palabra)
            es_primo = True 
            for divisor in range(1, palabra+1):
                if (palabra%divisor==0 and divisor!=1 and palabra!=divisor):
                    es_primo = False
                    break
            if(es_primo):
                numero.append(palabra)
            else: 
                print("Esto no es numero primo")
        else: 
            print("Esto no es un numero mayor a 0, por ende, no es un numero primo")
    elif(palabra == "stop"): 
        break 
    else: 
        print("Esto no es un numero natural ni la palabra \"stop\".")
resultado = 0
if(len(numero)>0):
    for contador in numero: 
        resultado += (contador*contador)
    print ("El resultado de la suma de los cuadrados es "+str(resultado))
else: 
    print("No ingresaste ningun numero primo.")

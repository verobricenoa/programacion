#Ejercicio 2. Anagramas. 
()
print("PROGRAMA PARA VERIFICAR SI DOS PALABRAS SON ANAGRAMAS")

#VARIABLES 
palabra_1=str(input("Ingrese una primera palabra: "))
palabra_2=str(input("Ingrese una segunda palabra: "))
cuenta_caracteres={}

#PARA VERIFICAR MAYUSCULAS Y ESPACIOS EN BLANCO 
palabra_1=palabra_1.lower().replace(" ","")
palabra_2=palabra_2.lower().replace(" ","")

print(f"usted ha ingresado {palabra_1} y {palabra_2}")

for caracter in palabra_1: 
    if caracter in cuenta_caracteres: 
        cuenta_caracteres[caracter]+=1
    else: 
        cuenta:caracteres=1
anagrama= True

for caracter in palabra_2: 
    if caracter not in cuenta_caracteres or cuenta_caracteres==0: 
        anagrama= False 
break

if anagrama : 
    print(f"Las palabras {palabra_1} y {palabra_2} SON ANAGRAMAS")
else: 
    print("Las palabras no son anagramas")
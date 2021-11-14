'''
Created on 25 abr. 2020

@author: PackardBell
'''



"""Funcion que arranca la aplicacion"""

def main():
    
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    letras = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
    
            
    while True:  #Bucle while principal
                
        
        dni = input("Por favor, introduzca su dni (escriba la letra en mayuscula): ")
        
        while True:
            dni = list(dni)
            
            if len(dni)==9:
                break
            else:
                print("El dni tiene que contener nueve caracteres")
                dni = input("Por favor, introduzca su dni: ")
         
            
        numerosDni = dni[:-1]        
                            
        contador = 0
        
        
        #Comprobamos si los ocho primeros caracteres son numeros, 
        #Cuando un caracter coincida con un numero, el contador aumentara en 1
        #El contador tiene que terminar valiendo 8 para que el formato dni sea correcto.   
          
        for caracter in numerosDni:   
            for n in numeros:
                if n == caracter:
                    contador+=1 
                                        
        
        letraValidada = "no" 
             
        letra = dni[len(dni)-1]
        
        
        #Comprobamos que el ultimo caracter del dni coincida con una letra
        
        for l in letras:
            if l == letra:
                letraValidada = "si"
                break
                            
                            
        #Si los 8 primeros caracteres son numeros y el ultimo es una letra, salimos del bucle 
          
        if contador==8 and letraValidada=="si":   
            print("Formato de dni correcto")
            break
        else:
            print("Formato de dni erroneo")
    
           
    dni = list(dni)  
            
    letra = dni[len(dni)-1]
    print("la letra es "+letra)
    
    
    cadenaNumeros = "".join(map(str, numerosDni))  # Transformamos la lista "numerosDni" en la cadena "cadenaNumeros
    numeros = int(cadenaNumeros)  #Transformamos la cadena "cadenaNumeros" en un entero "numeros"
    
        
    comprobacion(numeros,letra,letras)  #Llamamos al metodo comprobacion
     
 
 
 
"""Funcion que comprueba si el dni introducido 
por el usuario es autentico o falso"""    

def comprobacion(n,l,lista):
    resto = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
    r = n%23
    
    encontrado = "no"
    for indice in resto:
        if r==indice and l==lista[indice]:
            encontrado = "si"
            
    if(encontrado=="si"):
        print("El dni es verdadero")
    else:
        print("El dni es falso")    



main()





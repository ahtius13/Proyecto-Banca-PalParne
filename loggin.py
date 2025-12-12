import random

#Cada una de las funciones pide al usuario que ingrese el requisito en 3 intentos, cuando los 3 se cumplen se produce el loggin
#Lo suyo es que los usuarios esten en una lista de librerias con los datos personales de cada uno para comparar bien
#Cuando pasen los test correspondientes se puede proceder a la creación de un código en el main que llame a las funciones 

def nameclear(l):

    i = 0
    user = False

    while i <= 3:

     nameok = input("Por favor ingrese su nombre de usuario: ")
     
     if nameok in l:
            user = True
        
     else:
           nameok = input ("nombre de usuario incorrecto, por favor ingrese su nombre de usuario: ")
           i += 1
     
     return user
    
def passclear(l): 
 i = 0
 password = False

 while i <= 3:

     passok = input("Por favor ingrese su contraseña: ")
     
     if passok in l:
            password = True
        
     else:
           passok = input ("contraseña incorrecta, por favor ingrese su contraseña: ")
           i += 1
     
     return password
    
def codeclear(l):
  
  i = 0
  codesend = random.random(0000,9999)
  codepass = False

  while i <= 3:
     print(f"*En su dispositivo recive el siguiente mensaje* su código de ingreso es {codesend}")
     codeok = int(input("Por favor ingrese el código que ha recivido: "))
     
     if codeok == codesend:
            codepass = True
        
     else:
           codesend =random.random(0000,9999)
           print(f"*En el Dispositivo* código incorrecto, aquí su nuevo código {codesend}")
           codeok = int(input ("Por favor ingrese el nuevo código: "))
           i += 1
     
     return codepass
    




if __name__ == "__main__":

     
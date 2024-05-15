#Continuar con el video 70, en este video debemos de hacer, se debe estudiar lo que es el import regx, para poder
#realizar lo que es, las expresiones regulares, esto es importante, yua que en el codigo que se debe revisar debemos hacer
#o revisar lo que es el codigo de bancolombia.


import re

lista_nombres=['Ana Gomez',
               'Sebastian']

for elemento in lista_nombres:
    if re.findall('Sebastian', elemento):
        
        print(elemento)
        
        #Podemos realizar un match, para hacer declaraciones que permite
        #realizar coincidencias de patrones en datos
        
        
        
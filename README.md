Codigos de python: 

En primer lugar tenemos como lo mas basico de lo que es estar en python, mira te explico aqui podemos tener varios ejemplos:

print("Hola alumnos")
# Esto basicamente lo que hace es que imprime lo que has copiado dentro del print

#print("Hola alumnos"); print("Adios mundo cruel")
#Esto que es lo que haria, al tener el punto y coma daria un salto de linea, es decir, 
# La parte que dice Adios mundo cruel, quedaria abajo del hola alumnos

#mi_nombre="mi nombre es:" ("nombre")
#Esto lo que haria basicamente es que imprime en este caso el nombre que digites alli
#y a la hora de poner mi_nombre y le damos enter, apareceria el valor que le hemos dado a esa variable

#for i in range(5):
 #   a+=1
  #  print(a)
#El for en este caso lo utilizamos como un contador, ya que como podemos ver, a+=1
# La funcion que hace, que es la que esta en en el rango(range), definiria lo que es contar hasta 5 de 1 en 1

#if numero1>numero2:
 #   print("El numero mayor es 1")
#else:
 #   print("El numero mayor es 2")
    
    #En esta operacion podemos ver que existe una comparacion o mas bien tenemos una operacion donde verifica si un numero es mayor que otro
    
    #El if es una condicion, digamos que tiene un poco parecido con el while, la diferencia es que este te arroja resultados definitivos y directos, es decir,
    #las opciones ya estan definidas desde un principio, que quiero decir, que ya se le asigno una varible al if o al else, por lo tanto
    #Te arrojaria un resultado directo
    
  #  def mensaje():
        
   #     print("Conocimiento de python")
    #    print("Estamos en proceso de python")
        
    #mensaje()
    
    #El def es una funcion que puede llevar tanto parametros como argumentos, es decir, puedes definir la variable y entre los parentesis puedes poner una en especifico, ya sea para el ejercicio que este realizando
    #En este caso se estaria ejecutando lo que hay dentro del def, a que me refiero es a los prints que hay en el def, los ejecutaria tal cual estan definidos.
    #En el def puedes realizar todo tipo de operaciones, ya sea sumas, restas, etc...
    #Ahora bien recuerda que esto siempre y cuando llames la declaracion que tienes en el def
    
    
    #lista=["n1","n2","n3"]
    
    #En este apartado tenemos lo que son las listas, en este caso ya no definimos los requisitos por parentesis, sino que ya pasamos a lo que son los corchetes
    
    #Si pones print(nombre_de_la_lista), se te ejecutarian todos los parametros que tienes definidos en la lista
    
    #En las listas puedes definir que te salga un valor en especifico, pero ojo!!.
    
    #El conteo de los parametros en las listas empiezan desde 0, puedes prevenir esto para que no te lleves una sorpresa a la hora de ejecutar la lista.}
    
    #Tambien puedes poner que te salga desde una posicion hasta la otra, a que voy con esto, que puedes definir por ejemplo del 0 al 2
    
    #Lo harias de esta manera print(lista[0:2])
    #Cuando ejecutes esto te llevaria a lo que es desde la posicion 0 a la posicion 2, claramente esto depende de cuantos parametros hayas definido en la lista
    
    #Por este lado tenemos el insert, este comando sirve para como bien dice la palabra insertar un parametro a la lista y adicional, lo puedes añadir a una posicion
    
    #Aqui te muestro este ejemplo 
    
    #lista.insert(2,"n22")
    #print(lista)
    
    #Ahora a la hora de ejecutar esto te deberia aparecer el nuevo parametro insertado en la lista
    
    #En esta parte tenemos el extend, este es parecido al insert, la unica diferencia es que con este comando puedes meter todo tipo de dato, osea no es uno por uno, si quieres puedes meter tres parametros a tu lista, esta es la ventaja de este comando
    
    #lista.extend(["dato1","dato2","dato3"])
    #print(lista)
    
    #Ya cuando ejecutes te debe aparecer los nuevos parametros en la lista.
    
    #En esta parte tenemos el index, este comando a lo que va es a encontrar una posicion en una lista, lo puedes hacer de esta manera:
    
    #print(lista.index("dato1"))
    
    #Cuando ejecutes esto te deberia aparecer lo que es la posicion de este parametro
    
    #Tenemos el remove, este comando se utiliza para eliminar parametros de la lista, te muestro un ejemplo ya mismo
    
    #lista.remove("dato1")
    
    #print(lista)
    
    #Cuando ejecutes la operacion esto te deberia aparecer que ya este parametro no esta en la lista
    
    #Tenemos en esta parte lo que es las tuplas
    
    #La tupla la podriamos definir de una forma como una lista pero en este caso no solo estaran los parametros sino que en este caso tambien podran haber datos que describan un parametyro tal cual
    
    #Por ejemplo:
    
    #latuplaejemplo=["carlos", 16,4,1997]
    #print(latuplaejemplo)
    
    #Aqui ya te deberia ejecutar la tupla, es decir el valor que le asignaste a la tupla
    
    #podemos usar el len para hacer un conteo de lo que hay en la tupla
    
    #El len lo podemos usar para definir un numero de caracteres especifico
    
    #Por ejemplo: 
    
    #print(len(latuplaejemplo))
    
    #Cuando ejecutemos esto te deberia salir el conteo de todo lo que tienes en la tupla, es decir te cuenta cada una de las posiciones que hay en la tupla
    
    #Tambien podriamos hacer un empaquetado de tupla que en este caso seria lo mismo que hay en la tupla pero sin parentesis, esto te ejecutaria la tupla de igual manera
    
    #Tambien podriamos hacer puros print, que esto generaria lo mismo que hay en la tupla pero de forma vertical, es decir te aroja los parametros de forma vertical, a la hora de la ejecucion.
    
    #En este apartado tenemos lo que son los diccionarios:
    
    #Eldiccionario={"Colombia":"medellin"}
    #print(Eldiccionario["Colombia"])
    
    #A la hora de ejecutar esto te apareceria la ciudad que has puesto en el diccionario, y te preguntaras por que?
    
    #Muy bien mira la explicacion, cuando creamos el diccionario, como podemos ver esta la parte que dice colombia y la otra parte que dice medellin, pero si te fijas bien
    #Esto esta igualando el pais con la ciudad, entonces como en el print se puso Colombia, aparecera la ciudad del pais
    
    #Cabe recalcar que si pones el print, solo con el nombre del diccionario, solo aparecera los parametros que pusiste en el diccionario.
    
    #Podemos ejecutar otra lista, o bueno el mismo diccionario pero sin necesidad de estar en el mismo diccionario, me refiero a que lo puedes hacer un renglon mas abajo y lo que ejecutes ahi aparecera en el diccionario
    
    #Eldiccionario={"Colombia":"medellin"}
    #print(Eldiccionario["Colombia"])
    #Eldiccionario=["Rusia"]="Moscu"
    #print(Eldiccionario)
    
    #Cuando ejecutes esto te aparecera todo en el diccionario
    
    #Tenemos el comando del, el cual lo que hace es que ejecuta o borraria un parametro del diccionario
    
    #del Eldiccionario["Rusia"]
    #print(Eldiccionario)
    
    #Una vez ejecutes esto ya no tendria que aparecer en el diccionario lo que se definio en el del
    
    #Eldiccionario={"Colombia":"medellin"}
    #print(Eldiccionario.keys())
    #print(Eldiccionario.values())
    #print(Eldiccionario)
    
    #Muy bien aqui en este ejemplo tenemos lo siguiente, el keys es lo primario que tendria el diccionario.
    #El values, dice aja venga verifiquemos si todos los datos coinciden, osea que sean coherentes.
    #Por ultimo tenemos aqui el print de el diccionario, que es lo que lleva a cabo esto, ejecutaria todo el diccionario tal cual
    
    #En este apartado tenemos lo que es programacion orientada a objetos








    -----------------------------------------------------Programacion orientada a objetos------------------------------------------------------------------
#class Coche():
  
  
    def __init__(self):
      
      self._LargoChasis=250
     self.anchoChasis=120
     # self._ruedas=4
      #self._enmarcha=False
      
    #def arrancar(self,arrancamos):
     # self._enmarcha=arrancamos
      
      #if (self._enmarcha):
       # chequeo=self.cheque_interno()
      #if(self._enmarcha and chequeo):
       # return "El coche esta en marcha"
      
      #elif(self._enmarcha and chequeo==False):
       # return"Algo ha ido mal en el chequeo. no podemos arrancar"
      
      #else:
        
       # return "El coche esta parado"
      
      def estado(self):
        print("El coche tiene", self._ruedas, "ruedas. un ancho de", self._anchoChasis, "y un largo de"
            self.largoChasis)
        
        #def chequeo_interno(self):
         # print("Realizando chequeo interno")
          #self.gasolina="ok"
          #self.aceite="ok"
          #self.puertas="cerradas"
          
          #if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
           # return True
          
          #else:
            
           # return False
          
          
            
        #miCoche=Coche()
        
        #print(miCoche.arrancar(True))
        
        miCoche.estado()
        
        print(miCoche.chequeo_interno())
        
        "------------------aqui creamos el segunddo objeto---------------------"
        
        miCoche2=Coche()
        
        print(miCoche2.arrancar(False))
        
        miCoche2.estado()
        
        print(miCoche2.chequeo_interno())
        
        Aqui tenemos una clase creada

        A continuacion, pasaremos: a lo que son los temas de las clases en python:

        class Vehiculos():
  
  def __init__(self,marca,modelo):
    
    self.marca=marca
    self.modelo=modelo
    self.enmarcha=False
    self.acelera=False
    self.frena=False
    
  def arrancar(self):
    self.enmarcha=True
    
  def acelera(self):
    self.acelera=True
    
  def frenar(self):
    self.frenar=True
    
  def estado(self):
    print("Marca", self.marca, "\nModelo: ", self.modelo, "\en Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
    
class moto(Vehiculos):
    hcaballito=""
    
    def caballito(self):
      hcaballito="Voy haciendo caballito"
      print("Marca", self.marca, "\nModelo: ", self.modelo, "\en Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
    
      def estado(self):
       print("Marca", self.marca, "\nModelo: ", self.modelo, "\en Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
     
class Velectricos():
  def __init__(self):
    self.autonomia=100
    
  def cargarEnergia(self):
    self.cargando=True
    
    

miMoto = moto("Honda, CBR")

miMoto.caballito()

miMoto.estado()

miFurgoneta=Furgoneta=("Renault, Kangoo")

miFurgoneta.arrancar()

print(miFurgoneta.carga(True))

class BicicletaElectrica(Velectricos,Vehiculos):
  
  pass

miBici = BicicletaElectrica("Orbea", "HC1030")

# Que es lo que se esta haciendo en este codigo, basicamente se estan utilizando, funciones como constructores para definir lo que se esta haciendo en cada clase, como operaciones

A continuacion pasaremos a lo que es el manejo de archivos:

-------------------------------------------------------------------------------------------------------------------------

#from io import open

#archivo_texto=open("archivo.txt", "w")

#frase="Buen dia para estudiar python \n"

#archivo_texto.write(frase)




#from io import open

#archivo_texto=open("archivo_txt", "r")

#lineas_texto=archivo_texto.readlines()

#archivo_texto.close()

#print(lineas_texto[0])


#from io import open

#archivo_texto=open("archivo_txt", "r")

#archivo_texto.seek(11)

#print(archivo_texto.read())


#from io import open

#archivo_texto=open("archivo_txt", "r")


#archivo_texto.seek(len(archivo_texto.readline()))

#from io import open

#archivo_texto=open("archivo_txt", "r+")

#archivo_texto.write("comienzo del texto")

from io import open

archivo_texto=open("archivo_txt", "r+")

lista_texto=archivo_texto.readlines();

lista_texto[1]="Esta linea ha sido incluida desde el exterior \n"

archivo_texto.seek()

archivo_texto.writelines(lista_texto)

archivo_texto.close()

-------------------------------------------------------------------------------------------------------------------------------------------------




--------------------------- Por este lado tendriamos lo que son los modulos matematicos -------------------------------------

def sumar(op1,op2):
    print("El resultado es: ", op1+op2)
    
def restar(op1,op2):
    print("El resultado es: ", op1-op2)
    
def multiplicar(op1,op2):
    print("El resultado es: ", op1*op2)
    
def division(op1,op2):
    print("El resultado es: ", op1/op2)

------------------------------------------------------------------------------------------------------------------------------

Por este lado te mostrare como podemos hacer operadores matematicos:

import Modulos_matematicas

from Modulos_matematicas import sumar

Modulos_matematicas.sumar(7,5)

Modulos_matematicas.restar(4,9)

Modulos_matematicas.multiplicar(6,10)

#Cabe recalcar que en este ejercicio a la hora de importar ya sea lo que es sumar, restar, multiplicar o dividir, todo esto lo podemos hacer de forma
#poniendo los sgnos como por ejemplo, lo que es la suma(+), la resta(-) y asi sucesivamente, a la hora de importar un  modulo
#puedes poner el from y importar las matematicas


#Aqui si te fijas bien se utilizo, o mejor dicho se importo los modulos matematicos que se hicieron anteriormente

----------------------------------------------------------------------------------------------------------------------------------------------------------------------





Muy bien ahora dejando a un lado ese tema, te pondre este ejemplo de polimorfismo:


--------------------------------------------------------------------------------------------------------------------------------------------------------------

class Coche():
    
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")
        
class moto():
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")
        
class camion():
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")
        
def desplazamientoVehiculo(Vehiculo):
    Vehiculo.desplazamiento()
    
miVehiculo=moto()

desplazamientoVehiculo(miVehiculo)
    
    
    
        
miVehiculo=moto()

miVehiculo.desplazamiento()

miVehiculo2=Coche()

miVehiculo2.desplazamiento()

miVehiculo3=camion()

miVehiculo3.desplazamiento()

-------------------------------------------------------------------------------------------------------------------------------------------------------


Aqui te pondre una practica de strings:

-------------------------------------------------------------------------------------------------------------
nombreUsuario=input("Introduce tu nombre usuario")

print("El nombre es: ", nombreUsuario.lower())

print("El nombre es: ", nombreUsuario.capitalize())

edad=input("Introduce tu edad: ")

print(edad.isdigit())

--------------------------------------------------------------------------------------------------------------



Aqui te mostrare un ejemplo de lo que es la practica de filter:

def numero_par(num):
    if num % 2==0:
        return True
    
numeros = [17,23,45,67]

print(list(filter(lambda numero_par: numero_par%2==0, numeros)))

#Podriamos crear otro archivo de la funcion map, para aplicar una funcion a cada elemento de una o varias listas


Como tambien tenemos lo que es la practica del label

from tkinter import *

root=Tk

miFrame=Frame(root, width=500, height=400)

miImagen=PhotoImage(file="mouse.gif")

label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()


Vale, ahora te mostrare lo que es interfaz grafica, ojo no son funcionales, como bien dice es una interfaz grafica, mira te pongo algunos ejemplos:

from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)

miFrame.pack()

#---------------- Numero de pantalla -------------------------

numerodepantalla= StringVar()

pantalla=Entry(miFrame)
pantalla.grid(row=1, column=1, padx=10 ,pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")

# ------------------------- teclado -----------------------------

def numeropulsado (num):
    numerodepantalla.set(numerodepantalla.get()+ num)

#-----------------------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeropulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeropulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="8", width=3, command=lambda:numeropulsado("9"))
boton9.grid(row=2, column=3)
botonMult=Button(miFrame, text="x", width=3, command=lambda:numeropulsado("x"))
botonMult.grid(row=2, column=4)

#-----------------------fila 2 -------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeropulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeropulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeropulsado("6"))
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width=3)
botonMult.grid(row=3, column=4)

#---------------------------- fila 3 --------------------------


boton1=Button(miFrame, text="1", width=3, command=lambda:numeropulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeropulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeropulsado("3"))
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3, command=lambda:numeropulsado("-"))
botonRest.grid(row=4, column=4)

#-------------------- fila 4 ---------------------------------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeropulsado("0"))
boton0.grid(row=5, column=1)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeropulsado(","))
botonComa.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:numeropulsado("="))
botonIgual.grid(row=5, column=3)
botonSum=Button(miFrame, text="+", width=3, command=lambda:numeropulsado("+"))
botonSum.grid(row=5, column=4)



raiz.mainloop()

----------------------------------------------------------------------------------------------------------------

Otra interfaz grafica:

#from tkinder import *

#raiz=tk():
    
#raiz.title("Ventana de pruebas")

#raiz.resizable(True,False)

#raiz.iconbitmap("gato.ico")

#raiz.geometry("650x350")

#raiz.config(bg="blue")

#miFrame=Frame()

#miFrame.pack(side="right", anchor="s")

#miFrame.config(bg="red")

#miFrame.config(width="650", height="350")
    
#raiz.mainloop()

-------------------------------------------------------------------------------------------------------------------------------


Te mostrare como podemos crear un crud, obviamente esto si ya tienes una base de datos ya creada:

----------------------------------------------------------------------------------------------------------------------------------------------

from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()

barramenu=Menu(root)
root.config(menu=barramenu, width="300", height=300)

bbddmenu=Menu(barramenu, tearoff=0)
bbddmenu.add_command(Label="Conectar")
bbddmenu.add_command(Label="Salir")

borrarMenu=Menu(barramenu, tearoff=0)
borrarMenu.add_command(Label="Borrar_campos")

crudMenu=Menu(barramenu, tearoff=0)
crudMenu.add_command(Label="Crear")
crudMenu.add_command(Label="Actualizar")
crudMenu.add_command(Label="Leer")
crudMenu.add_command(Label="Borrar")

ayudamenu=Menu(barramenu, tearoff=0)
ayudamenu.add_command(Label="Licencia")
ayudamenu.add_command(Label="Acerca de...")

barramenu.add_cascade(Label="BBDD", menu=bbddmenu)
barramenu.add_cascade(Label="BBDD", menu=borrarMenu)
barramenu.add_cascade(Label="BBDD", menu=crudMenu)
barramenu.add_cascade(Label="BBDD", menu=ayudamenu)

#Este crud se podria utilizar como ejemplo si ya tienes en algo en que comkplementarlo, te pongo un ejemplo, creaste una interfaz donde pusiste
#id, nombre, apellido, etc...

#Que tienes que hacer en este punto debes inicializar los campos, lo debes hacer con grid, tambien le puedes meter un config, y como no dar pase al entry
#Que en este caso es en el que se ha estado trabajando que es el miFrame

#Los puedes validar uno por uno dependiendo de los campos que allas puesto, me refiero a los label.

#Obviamente el crud lo podemos meter a una base de datos, es decir podriamos inicializar en base de datos a ese punto voy

#Podemos crear varios (def), que podriamos poner para diferente campon te pongo un ejemplo

#Digamos que ya tu tienes tu base de datos implementada, ahora bien el def en el codigo lo podrias utilizar de esta forma

#def limpiarcampos():
    #Digamos que pusiste en tu interfaz, id
 #   miId.set("")
 
 #Con este comando podrias inicializar lo que es la limpieza de los campos
 
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Te mostrare lo que es la serializacion:

-------------------------------------------------------------------------------------------------------------------------------------------------------

 #import pickle

#lista_nombres=["Pedro","Ana","Maria", "Isabel"]

#fichero_binario=open("Lista_nombres", "wb")

#pickle.dump(lista_nombres, fichero_binario)

#fichero_binario.close()

#del (fichero_binario)

import pickle

fichero=open("lista_nombres", "rb")

lista=pickle.load(fichero)

print(lista)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Como podemos serializar objetos:

--------------------------------------------------------------------------------------------------------------------------------------------------

#En la serializacion tendriamos que importar pickle

#import pickle

#fichoApertura=open("LosCoches", "rb")

#misCoches=pickle.load(ficheroApertura)

#fichoApertura.close()

#for c in misCoches:
    
 #   print(c.estados())
    
    #Basicamente lo que se hizo aqui fue implementar un tipo de serializacion, aunque no este implementado en el ejercicio que esta 
    #en el archivo de pythpn llamado pro_objetos, este seria el proceso que se tendria que hacer

----------------------------------------------------------------------------------------------------------------------------------------------------

Te tengo un ejemplo de lo que es setup:


from setuptools import setup

#setup(
    
   # name="paquetePractica_setup",
    #version=1.0,
    #description="paquete de operaciones matematicas",
    #author="Torres"
    #author_email="grisalesjohao@gmail.com"
    #packages=["Practicas_setup"]
    
    #Estudiar sobre paquetes distribuibles
    
#)

---------------------------------------------------------------------------------------------------------------------------------------------------

Aqui te tengo un ejemplo de bbdd (Base de datos)

---------------------------------------------------------------------------------------------------------------------------------------------------

import sqlite3

miConexion=sqlite3("Mi primera base de datos")

miCursor= miConexion.cursor()

miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR, PRECIO INTEGER, SECCION VARCHAR(20)")

#Ya en este punto tenemos creada la base de datos, muy bien ahora nos podemos hacer de cuenta que estamos trabajando
#en mysql o phpmyadmin, donde ejecutamos los comandos de forma comun y corriente

#Ahora te preguntaras si eres una persona que conoces lo que es phpmyadmin, seguramente reconoceras lo que significa
#El create table, pero en este caso utilizaremos el insert into, que seria para meter nuevos datos a la base de datos

#Podemos usar el drop table para borrar, y tambien podemos usar el selct * from, para seleccionar un dato en especifico de una tabla

#Ahora bien podemos utilizar el fetchall, que se utiliza para mostrar una tabla por completo, es decir, te puedo poner un ejemplo

#Podemos crear esto mira te pongo un ejemplo:

# 

#Productos_nuevos

#varios_productos[
 #   ("Camiseta", 3, "Adidas")
#]

#Muy bien, ya en este punto podemos crear el fetchall, el cual nos dejaria ver los datos en la tabla de la base de datos


#Con el comando executemany, podriamos crear lo que es el insert into y validar los datos que se estan verificando en ese momento

#Podemos utilizar el update tambien para ejecutar una tabla que no tenga los datos actualizados, esto tambnien lo podemos hacer con el execute

#Podemos utilizar tambien el delete from con el mismo comando, este comando se usa mas que todo para ejecutar o mejor dicho oara eliminar un dato en especifico de una tabla


miConexion.close()

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Te tengo un ejemplo de lo que es doctest:

--------------------------------------------------------------------------------------------------------------------

def areaTriangulo(base,altura):
    
    #Calcula el area de un triangulo dado
    
    #>>> areaTriangulo(3,6)
    #'El area del triangulo es: 9.0'
    
    #>>> areaTriangulo(4,5)
    #'El area del triangulo es: 10.0'
    
    return "El area del triangulo es: "+str((base*altura)/2)

import doctest
doctest.testmod()

#Podemos importar math para que podamos hacer operaciones avanzadas de matematicas

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Aqui tenemos un ejemplo de entry:

---------------------------------------------------------------------------------------------------

from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

cuadroTexto=Entry(miFrame)
cuadroTexto.place(x=100, y=100)
nombreLabel(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0)

raiz.mainloop()


#Podemos hacer un label para cada uno de los datos que se requieran, es decir, se puede hacer de forma en que podamos poner el nombre, apellido, etc...


#Le podemos poner un config, para modificar ya sea el nombre ponerle el color o centrar el texto de lo que se esta copiando

#Podemos agregar un scrollvert para crear una especie de cursor en el texto que se copie

#Podemos crear un boton llamado button, donde podemos modificar o poner una funcion para enviar un dato

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Aqui tenemos un ejemplo de lo que seria un infoPermanente:

-------------------------------------------------------------------------------------------------------------------------------

import pickle

#class persona():
    
  #  def __init__(self, nombre, genero, edad):
  #   self.nombre=nombre()
   #     self.genero=genero()
    #    self.edad=edad()
     #   print("Se ha creado una persona nueva con el nombre de", self.nombre)
        
      #  def __str__(self):
       #     return "{} {} {}".format(self.nombre, self.genero, self.edad)
        
        #class ListaPersonas:
         #   personas=[]
            
          #  def __init__(self):
                
           #     Lista_de_personas=open("Fichero externo", "ab")
            #    ListaPersonas.seek(0)
                
            #try:
                
             #   self.personas=pickle.load(Lista_de_personas)
              #  print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
            #except:
            #    print("El fichero esta vacio")
            #finally:
             #   ListaPersonas.close()
              #  del(ListaPersonas)
            #def agregarPersonas(self,p):
             #   self.personas.append(p)
                
            #def mostrarPersonas(self):
             #   for p in self.personas:
              #      print(p)
                    
            #def guardarPersonasEnFicherosExternos(self):
             #   ListaPersonas=open("Fichero externo", "wb")
              #  pickle.dump(self.personas, ListaPersonas)
               # ListaPersonas.close()
                #del(ListaPersonas)
                
         #   def mostrarInfodeFicheroExterno(self):
          #      print("La informacion del fichro es la siguiente: ")
           #     for p in self.personas:
            #        print(p)
                    
        #milista_personas=ListaPersonas()
        #p=persona("Carlos", "masculino", 35)
        #milista_personas.agregarPersonas(p)
        #p=persona("Antonio", "masculino", 45)
        #milista_personas.agregarPersonas(p)
        #p=persona("Zion", "Masculino", 32)
        #milista_personas.agregarPersonas(p)
      
-----------------------------------------------------------------------------------------------------------------------------------------------------------
















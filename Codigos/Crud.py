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
 
 
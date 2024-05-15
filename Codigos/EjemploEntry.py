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
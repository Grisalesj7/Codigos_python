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












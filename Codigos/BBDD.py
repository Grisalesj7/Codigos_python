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
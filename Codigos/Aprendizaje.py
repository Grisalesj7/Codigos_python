#print("Hola alumnos")
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
    
    #Continuar con el video nro 29 para mañana dia jueves y seguir con los videos que siguen de ahi para alla 
    
    #En este apartado tenemos lo que es programacion orientada a objetos
    
#class Coche():
  
  
  #  def __init__(self):
      
   #   self._LargoChasis=250
    #  self.anchoChasis=120
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
      
      #def estado(self):
       # print("El coche tiene", self._ruedas, "ruedas. un ancho de", self._anchoChasis, "y un largo de"
        #    self.largoChasis)
        
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
        
        #miCoche.estado()
        
        #print(miCoche.chequeo_interno())
        
        #"------------------aqui creamos el segunddo objeto---------------------"
        
        #miCoche2=Coche()
        
        #print(miCoche2.arrancar(False))
        
        #miCoche2.estado()
        
        #print(miCoche2.chequeo_interno())
        
        #Aqui tenemos una clase creada
        
        
        #A continuacion:
        
        
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
  


  
    
    
        
        
        
        
        
     
    
    
    
    














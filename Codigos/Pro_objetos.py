"----------------Este es un ejemplo de una clase--------------------"
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
"-----------------------Este seria el fin del primer ejemplo------------------------------------"       
        #Aqui tenemos una clase creada
        
        
        #A continuacion:
        
"---------------------------Este seria el inicio del segundo ejemplo-----------------------------"  

import pickle

      
#class Vehiculos():
  
 # def __init__(self,marca,modelo):
    
  #  self.marca=marca
   # self.modelo=modelo
    #self.enmarcha=False
    #self.acelera=False
    #self.frena=False
    
  #def arrancar(self):
   # self.enmarcha=True
    
  #def acelera(self):
   # self.acelera=True
    
  #def frenar(self):
   # self.frenar=True
    
  #def estado(self):
   # print("Marca", self.marca, "\nModelo: ", self.modelo, "\en Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
    
#class moto(Vehiculos):
 #   hcaballito=""
    
  #  def caballito(self):
   #   hcaballito="Voy haciendo caballito"
    #  print("Marca", self.marca, "\nModelo: ", self.modelo, "\en Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
    
    #  def estado(self):
     #  print("Marca", self.marca, "\nModelo: ", self.modelo, "\en Marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)
     
#class Velectricos():
 # def __init__(self):
  #  self.autonomia=100
    
  #def cargarEnergia(self):
   # self.cargando=True
    
    

#miMoto = moto("Honda, CBR")

#miMoto.caballito()

#miMoto.estado()

#miFurgoneta=Furgoneta=("Renault, Kangoo")

#miFurgoneta.arrancar()

#print(miFurgoneta.carga(True))

#class BicicletaElectrica(Velectricos,Vehiculos):
  
 # pass

#miBici = BicicletaElectrica("Orbea", "HC1030")


"----------------------Este seria el fin del segundo ejemplo----------------------------"



"-------------------------Este seria el inicio del tercer ejemplo------------------------"

#class Persona():
 #   def __init__(self, nombre, edad, lugar_de_residencia):
        
  #      self.nombre=nombre
   #     self.edad=edad
    #    self.lugar_de_residencia=lugar_de_residencia
        
        
#class empleado(Persona):
    
 #   def __init__(self,salario,antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        
 #      super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        
  #      self.salario=salario()
   #     self.antiguedad=antiguedad()
        
    #def descripcion(self):
     #  super().descripcion()
      # print("Salario: " self.salario, "Antiguedad: ", self.antiguedad)
        
        
#Antonio=Persona(1000,10,"Antonio", 43, "Medellin")

"-------------------------------------este seria el fin del tercer ejemplo--------------------------------"






        
        


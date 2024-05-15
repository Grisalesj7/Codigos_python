#Aqui realizaremos un ejemplo de polimorfismo

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
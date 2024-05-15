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
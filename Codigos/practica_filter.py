def numero_par(num):
    if num % 2==0:
        return True
    
numeros = [17,23,45,67]

print(list(filter(lambda numero_par: numero_par%2==0, numeros)))

#Podriamos crear otro archivo de la funcion map, para aplicar una funcion a cada elemento de una o varias listas
numeros = [1,2,3,4,5,6,7,8,9,10]
lista = []
    
for i in numeros:
    if i == 4 or i == 7 or i == 9:
        lista.append(numeros[i] * 2)              
for i in lista:
    print(f"{i}")

def tabla_mulplicar():
    n=int(input("Por favor introduzca un numero entero entre 1 y 10: "))

    #Se crea el archivo txt.
    file_name="tabla-n" + str(n) + '.txt'
    f=open(file_name,"w") 

    for i in range(1,11):
        f.write(str(n) + 'x' + str(i) + "=" + str(n*i) + "\n")
    f.close()

tabla_mulplicar()
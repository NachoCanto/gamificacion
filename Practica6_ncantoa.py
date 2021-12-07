from os.path import exists

def read_table_multiplicar():
    n=int(input("Introduzca un numero entero entre 1 y 10: "))# usamos int
    file_name="tabla-n" + str(n) + ".txt"  #Se crea el .txt

    try:
        f=open(file_name,"r")
    except FileNotFoundError:
        print("No existe el fichero con la tabla del: ",n)
    else:
        print(f.read())

read_table_multiplicar() 
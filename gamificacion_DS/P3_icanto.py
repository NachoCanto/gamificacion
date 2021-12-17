def ataque3():

    gadgets = ["Batería", "Portátil", 100, "Ordenador central", 310.28,"Altavoces", 27.00, "Pantalla", 1000, "Maletín electrónico", "Lente de cámara"]
    numeros = []
    cadena = []

    for i in gadgets:
        if type(i) == float or type(i) == int:
            numeros.append(i)
        else:
            cadena.append(i)

    print(f"\n\tcadena ordenadas en ascenso:  {sorted(cadena)}")
    print(f"\tcadena ordenadas en ascenso:  {sorted(cadena, reverse = True)}")
    print(f"\tNúmeros ordenados de menor a mayor:  {sorted(numeros, reverse = True)}")
    print(f"\tNúmeros ordenados de mayor a menor:  {sorted(numeros)}\n")

ataque3()

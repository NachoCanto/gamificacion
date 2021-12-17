def ataque2():

    caracteres = input(f"Pon una lista de caracteres separados por comas (,):  ")

    caracteresNoRepetidos = caracteres.split(",")

    print(f"\n\t{set(caracteresNoRepetidos)}\n")

ataque2()
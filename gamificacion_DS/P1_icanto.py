def ataque1():
    from num2words import num2words

    count = 0
    numbers = []
    sumx9 = 0

    while True:
        
        number = int(input(f"Introduce un número entre 10 y 99: "))

        if number > 9 and number < 100:
            numbers.append(number)
            count += number
        
        continu = input(f"\tQuieres introducir otro número (y / n): ").lower()

        if continu.startswith("n"):
            break

    print(f"\tLa suma de los números es {num2words(count)}")
    for i in range(len(numbers)):
        sumx9 += numbers[i]*9
    print(f"\tLa suma de los números multiplicados x 9 es: {num2words(sumx9)}")
    print(f"\tEl mayor número es {num2words(max(numbers))} y el menor es {num2words(min(numbers))}")
    print(f"\tHas introducido {num2words(len(numbers))} números")

ataque1()
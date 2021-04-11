if __name__ == '__main__':
    numero1 = int(input("Digite o valor do numero1: "))
    numero2 = int(input("Digite o valor do numero2: "))
    numero3 = int(input("Digite o valor do numero3: "))

    if numero1 > numero2 and numero1 > numero3:
        print("o maior entre eles é: " + str(numero1))
    elif numero2 > numero1 and numero2 > numero3:
        print("o maior entre eles é: " + str(numero2))
    else:
        print("o maior entre eles é: " + str(numero3))
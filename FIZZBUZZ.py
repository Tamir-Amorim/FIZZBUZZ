

entrada = int(input("Informe um número\n"))

for i in range(1, entrada +1 ):
    if i % 15 == 0:
        print("BUZZFIZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")

    else: print(i)



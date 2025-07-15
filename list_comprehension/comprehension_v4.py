generator = (i ** 2 for i in range(15) if i % 2 == 1)

for numero in generator:
    print(numero)

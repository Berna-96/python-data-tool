def calcola_media(numeri):
    return sum(numeri) / len(numeri)

def calcola_massimo(numeri):
    massimo = numeri[0]
    for n in numeri:
        if n > massimo:
            massimo = n
    return massimo

def calcola_minimo(numeri):
    minimo = numeri[0]
    for n in numeri:
        if n < minimo:
            minimo = n
    return minimo

numeri = [10, 5, 8, 20, 3]

print("Media:", calcola_media(numeri))
print("Massimo:", calcola_massimo(numeri))
print("Minimo:", calcola_minimo(numeri))

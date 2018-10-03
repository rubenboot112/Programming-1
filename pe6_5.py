grondgetallen = [1, 8, 12, -5, -7, 4, -9, 2]

def kwadraten_som():
    kwadraten = []
    for i in grondgetallen:
        if i > 0:
            kwadraten.append(i ** 2)
    return kwadraten

print(kwadraten_som())
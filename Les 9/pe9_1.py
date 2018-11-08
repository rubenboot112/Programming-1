invoer=0
som=0
while True:
    getal = int(input("Geef een getal: "))
    invoer += 1
    som += getal
    if getal == 0:
        print("Er zijn {} getallen ingevoerd, de som is: {}".format(invoer, som))
        break
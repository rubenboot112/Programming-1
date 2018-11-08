def gemiddelde(zin):
    som = 0
    for i in zin.split(" "):
        som += len(i)
    return som / len(zin.split(" "))

print ("Gemiddelde lengte van de woorden in de zin: {:.0f}".format(gemiddelde(input("Typ een willekeurige zin: \n"))))
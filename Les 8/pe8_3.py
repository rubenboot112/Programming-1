def getallen(string):
    list = (sorted(map(int, string.split("-"))))
    print ("Gesorteerde list van ints: {}\nGrootste getal: {} en Kleinste getal: {}\nAantal getallen: {} en Som van de getallen: {}\nGemiddelde: {}".format(list, max(list), min(list), len(list), sum(list), sum(list) / len(list)))





invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
getallen(invoer)
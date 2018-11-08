bruin = {"Boxtel", "Best", "Beukenlaan", "Eindhoven", "Helmond 't Hout", "Helmond", "Helmond Brouwhuis", "Deurne"}
groen = {"Boxtel", "Best", "Beukenlaan", "Eindhoven", "Geldrop", "Heeze", "Weert"}
print ("Trajecten Bruin en Groen komen allebij langs: ")
for i in bruin.intersection(groen):
    print (i, end=", ")
print ("\n\nTraject Bruin verschilt met traject Groen: ")
for i in bruin.difference(groen):
    print (i, end=", ")
print ("\n\nTraject van Bruin: ")
for i in bruin:
    print (i, end=", ")
print ("\n\nTrajecten van Groen: ")
for i in groen:
    print (i, end=", ")
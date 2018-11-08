infile = open("Kaartnummers.txt", "r")
list = []
kaartnummers = infile.read().split("\n")
for i in kaartnummers:
    list += [(i.split(",")[0])]
print ("Deze file telt {} regels\nHet grootste kaartnummer is: {} en dat staat op regel {}".format(len(kaartnummers), max(list), list.index(max(list)) + 1))
infile.close()
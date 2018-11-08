infile = open("Kaartnummers.txt", "r")
kaartnummers = infile.readlines()
for i in kaartnummers:
    print("{} {} {}".format(str(i.split(",")[1])[:-1], "heeft kaartnummer: ", i.split(",")[0]))
infile.close()
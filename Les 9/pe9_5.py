dict = {}
def namen(naam):
    if naam in dict:
        dict[naam] = dict.get(naam) + 1
    else:
        dict[naam] = 1

while True:
    naam = input("Volgende naam: ")
    if naam != "":
        namen(naam)
    else:
        for i in dict:
            if dict.get(i) == 1:
                print("Er is {} student met de naam {}".format(dict.get(i), i))
            else:
                print("Er zijn {} studenten met de naam {}".format(dict.get(i), i))
        break
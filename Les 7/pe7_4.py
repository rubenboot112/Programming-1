import datetime
outfile = open("Hardlopers.txt", "a")
naam = ""
while naam != "q":
    naam = input("(Als je wilt stoppen voer 'q' in) Naam: ")
    if naam != "q":
        vandaag = datetime.datetime.today()
        outfile.write("{}, {}\n".format(vandaag.strftime("%a %d %b %Y, %H:%M:%S"), naam))

else:
    outfile.close()
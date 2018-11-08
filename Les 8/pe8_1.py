def seizoen(maand):
    if maand == 12 or maand <= 2:
        print ("{}: {}".format(maand, "Winter"))
    elif maand <= 5:
        print("{}: {}".format(maand, "Lente"))
    elif maand <= 8:
        print("{}: {}".format(maand, "Zomer"))
    else:
        print("{}: {}".format(maand, "Herfst"))


for i in range(1,13):
    seizoen(i)

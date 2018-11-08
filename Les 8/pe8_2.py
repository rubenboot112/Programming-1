def new_list(oldlist):
    newlist = []
    if len(oldlist) >= 4:
        for words in oldlist:
            if len(words) <= 4:
                newlist += [words]
        print (newlist)
    else:
        print("Minimaal 10 strings!")


list = eval(input("Geef lijst met minimaal 10 strings: "))
new_list(list)
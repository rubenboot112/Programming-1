cijfers = {8 : "Piet", 4 : "Jan", 2 : "Fred", 10 : "Nic", 9 : "Rik", 9.4 : "Henk", 3 : "Koen", 5.5 : "Tim"}
for cijfer in cijfers:
    if cijfer >= 9:
        print("{} {}".format(cijfer, cijfers[cijfer]))
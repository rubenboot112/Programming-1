import random

def monopolyworp():
    for i in range(3):
        dobbel1 = random.randint(1, 9)
        dobbel2 = random.randint(1, 9)
        if dobbel1 == dobbel2:
            if i == 2:
                print("{} + {} = {} (direct naar gevangenis)".format(dobbel1, dobbel2, dobbel1 + dobbel2))
            else:
                print("{} + {} = {} (dubbel)".format(dobbel1, dobbel2, dobbel1 + dobbel2))
        else:
            print("{} + {} = {}".format(dobbel1, dobbel2, dobbel1 + dobbel2))
            break

monopolyworp()
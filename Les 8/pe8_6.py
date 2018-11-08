def menu():
    print("\n1: Ik wil weten hoeveel kluizen nog vrij zijn")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen ")
    print("4: Ik geef mijn kluis terug")
    print("5: Stoppen\n")
    menukeuze = input("Kies een optie (1-5): ")
    if menukeuze == "1":
        toon_aantal_kluizen_vrij()
    elif menukeuze == "2":
        nieuwe_kluis()
    elif menukeuze == "3":
        kluis_openen()
    elif menukeuze == "4":
        kluis_teruggeven()
    elif menukeuze == "5":
        exit()
    else:
        print("Verkeerde invoer!")
        menu()


def toon_aantal_kluizen_vrij():
    file = open("kluizen.txt", "r")
    beschikbaar = 12 - len(file.readlines())
    if beschikbaar == 0:
        print("\nEr zijn geen kluizen meer beschikbaar")
    elif beschikbaar == 1:
        print("\nEr is nog 1 kluis beschikbaar")
    else:
        print("\nEr zijn nog {} kluizen beschikbaar".format(beschikbaar))
    file.close()
    menu()


def nieuwe_kluis():
    file = open("kluizen.txt", "r+")
    kluizen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    for nkluis in file.readlines():
        for kluis in kluizen:
            if int((nkluis.split(";")[0])) == kluis:
                kluizen.remove(kluis)
    if not kluizen:
        print("Er zijn geen kluizen meer beschikbaar!")
    else:
        code = input("Voer een code in voor u kluis: ")
        file.write("\n{};{}".format(kluizen[0], code))
        print ("U heeft een nieuwe kluis met kluisnummer: {}".format(kluizen[0]))
    file.close()
    menu()


def kluis_openen():
    try:
        kluisnummer = int(input("Wat is uw kluisnummer?: "))
        if kluisnummer >= 1 and kluisnummer <= 12:
            file = open("kluizen.txt", "r")
            kluiscn = {}
            for i in file.readlines():
                kluiscn[i.split(";")[0]] = i.split(";")[1].replace("\n", "")
            if str(kluisnummer) in kluiscn:
                kluiscode = input("Wat is uw kluiscode?: ")
                if kluiscode == kluiscn.get(str(kluisnummer)):
                    print("kluis {} geopend!".format(kluisnummer))
                else:
                    print("Verkeerde code voor kluis {}".format(kluisnummer))
            else:
                print("Deze kluis is nog niet gebruikt!")
            file.close()
            menu()
        else:
            print("Kies een kluis van 1 t/m 12")
            kluis_openen()
    except ValueError:
        print ("Verkeerde invoer!")
        kluis_openen()


def kluis_teruggeven():
    try:
        kluisnummer = int(input("Wat is uw kluisnummer?: "))
        file = open("kluizen.txt", "r+")
        if kluisnummer >= 1 and kluisnummer <= 12:
            kluiscn = {}
            for i in file.readlines():
                kluiscn[i.split(";")[0]] = i.split(";")[1].replace("\n", "")
            if str(kluisnummer) in kluiscn:
                kluiscode = input("Wat is uw kluiscode?: ")
                if kluiscode == kluiscn.get(str(kluisnummer)):
                    file.seek(0)
                    lines = file.readlines()
                    file.seek(0)
                    file.truncate()
                    for line in lines:
                        if line != str(kluisnummer) + ";" + kluiscode and line != str(
                                kluisnummer) + ";" + kluiscode + "\n":
                            file.write(line)
                    file.close()
                    print("Kluis {} is terug genomen!".format(kluisnummer))
                else:
                    print("Verkeerde code voor kluis {}".format(kluisnummer))
            else:
                print("Kluis {} is al vrij!".format(kluisnummer))
            menu()
        else:
            print("Kies een kluis van 1 t/m 12")
            kluis_teruggeven()
    except ValueError:
        print("Verkeerde invoer!")
        kluis_teruggeven()


menu()
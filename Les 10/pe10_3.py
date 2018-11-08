def code(invoerstring):
    beveiliging = ""
    for i in invoerstring:
        beveiliging += chr(ord(i)+3)
    return  beveiliging

print (code(input("Voer in gebruiker+beginstation+eindstation: ")))
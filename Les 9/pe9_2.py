while True:
    string = input("Geef een string van vier letters: ")
    if len(string) == 4:
        print("Inlezen van correcte string: {} is geslaagd".format(string))
        break
    else:
        print("{} heeft {} letters".format(string, len(string)))
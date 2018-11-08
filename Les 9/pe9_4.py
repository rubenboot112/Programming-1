def tinker(filename):
    file = open(filename, "r")
    dict = {}
    lines = file.readlines()
    for line in lines:
        dict.update({line.split(":")[0] : line.split(":")[1].replace("\n", "")})
    file.close()
    return dict





companyname = input("Enter Company name: ")
print (tinker("pe9_4.txt").get(companyname, "Company name does not excist."))
tinkersymbol = input("\nEnter Tinker symbol: ")
for item in list(tinker("pe9_4.txt").items()):
    if tinkersymbol in item:
        print(item[0])
        q = False
        break
    else:
        q = True
if q == True:
    print ("Tinker symbol doest not excist")

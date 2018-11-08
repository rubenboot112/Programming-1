def inlezen_beginstation(stations):
    while True:
        inp_beginstation = input("Wat is je beginstation?\n>> ")
        if inp_beginstation in stations:
            return inp_beginstation
            break
        else:
            print("Station bestaat niet in dit traject!\n")

def inlezen_eindstation(stations, beginstation):
    while True:
        inp_eindstation = input("Wat is je eindstation?\n>> ")
        if inp_eindstation in stations:
            if stations.index(inp_eindstation) > stations.index(beginstation):
                return inp_eindstation
                break
            elif beginstation == inp_eindstation:
                print("Je stapt al in op station {}\n".format(inp_eindstation))
            else:
                print("Dit station is voor station: {}\n".format(beginstation))
        else:
            print("Station bestaat niet in dit traject!\n")

def omroepen_reis(stations, beginstation, eindstation):
    print("\nHet beginstation {} is het {}e station in het traject.".format(beginstation, stations.index(beginstation) + 1))
    print("Het eindstation {} is het {}e station in het traject.".format(eindstation, stations.index(eindstation) + 1))
    print("De afstand bedraagt {} station(s).".format(stations.index(eindstation) - stations.index(beginstation)))
    print("De prijs van het kaartje is {} euro.".format((stations.index(eindstation) - stations.index(beginstation)) * 5 ))
    print("\nJij stapt in de trein in: {}".format(beginstation))
    for i in range(stations.index(beginstation)+1, stations.index(eindstation)):
        print(" - {}".format(stations[i]))
    print("Jij stapt uit in: {}".format(eindstation))


stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)

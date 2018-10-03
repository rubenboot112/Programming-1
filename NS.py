def standaardprijs(afstandKM):
    if afstandKM >= 50:
        result = afstandKM * 0.6 + 15
        return result
    elif afstandKM < 0:
        result =  afstandKM * 0
        return result
    else:
        result = afstandKM * 0.8
        return result

def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardprijs(afstandKM)
    if 12 < leeftijd >= 65:
        standaardprijs(afstandKM) * 0.7

    if weekendrit == 'ja' and 12 < leeftijd >= 65:
        standaardprijs(afstandKM) * 0.65
    if weekendrit == 'ja' and 12 >= leeftijd < 65:
        standaardprijs(afstandKM) * 0.6

    return standaardprijs(afstandKM)
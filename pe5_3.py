leeftijd = int(input('Geef je leeftijd: '))
paspoort = str(input('Nederlands paspoort: '))

if leeftijd >= 18 and paspoort == 'ja':
    print('Je mag stemmen!')
else:
    print('Je mag niet stemmen!')
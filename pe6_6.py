lijst = ['a', 'b', 'c']

def wijzig(a):
    a.clear()
    a.append('d')
    a.append('e')
    a.append('f')
    return a

print(lijst)
wijzig(lijst)
print(lijst)
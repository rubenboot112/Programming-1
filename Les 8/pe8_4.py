studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
   antw = []
   for i in studentencijfers:
       antw += [sum(i) / len(i)]
   return antw
def gemiddelde_van_alle_studenten(studentencijfers):
    antw = sum(gemiddelde_per_student(studentencijfers)) / len(studentencijfers)
    return int(antw)



print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))
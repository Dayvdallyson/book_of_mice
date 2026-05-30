people = [ "Carlos", "Amanda", "Bruno", "Ana", "Fernanda", "Arthur", "Daniel", "Camila", "André", "Bianca", "Felipe", "Alice", "Gabriel", "Aline", "Rafael", "Beatriz", "Augusto", "Marina", "Caio", "Alberto"]

people_with_a = []

for person in people:
    if person[0].lower() == "a":
        people_with_a.append(person)

print(people_with_a)

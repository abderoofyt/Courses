names = []
birthdays = []

with open('DOB.txt', 'r', encoding="utf-8") as file:
    for line in file:
        parts = line.split()
        
        name = " ".join(parts[:-2])
        birthday = " ".join(parts[-2:])
        
        names.append(name)
        birthdays.append(birthday)

print("Names:")
for name in names:
    print(name)

print("\nBirthdays:")
for birthday in birthdays:
    print(birthday)

choice = input("Choose '1' for alternate characters or '2' for alternate words: ")
text = input("Enter a sentence: ")

if choice == "1":
    result = ""
    for i, char in enumerate(text):
        if i % 2 == 0:
            result += char.upper()
        else:
            result += char.lower()
    print(result)

elif choice == "2":
    words = text.split()
    for i in range(len(words)):
        if i % 2 == 0:
            words[i] = words[i].lower()
        else:
            words[i] = words[i].upper()
    print(" ".join(words))

else:
    print("Invalid choice! Please enter '1' or '2'.")

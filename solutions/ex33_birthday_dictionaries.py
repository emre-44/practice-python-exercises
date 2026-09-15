def get_birthday():
    birthdays = {
    "Albert Einstein": "March 14, 1879",
    "Benjamin Franklin": "January 17, 1706",
    "Ada Lovelace": "December 10, 1815"
}
    print("Welcome to the birthday dictionary. We konw the birthdays of: ")
    for name in birthdays:
        print(name)

    name = input("Who's birthday do you want to look up? \n")

    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}")
    else:
        print(f"Sorry, we dont have {name}'s birthday.")

print(get_birthday())
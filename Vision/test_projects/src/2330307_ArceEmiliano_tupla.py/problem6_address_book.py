# Problem 6: Simple address book (CRUD)

contacts = {
    "Emix": "1234567890",
    "Bryan": "5551234567"
}

action_text = "SEARCH".strip().upper()
name = "Emix".strip().title()

if action_text == "ADD":
    phone = "9998887777".strip()
    contacts[name] = phone
    print("Contact saved:", name, phone)

elif action_text == "SEARCH":
    if name in contacts:
        print("Phone:", contacts[name])
    else:
        print("Error: contact not found")

elif action_text == "DELETE":
    if name in contacts:
        contacts.pop(name)
        print("Contact deleted:", name)
    else:
        print("Error: contact not found")

else:
    print("Error: invalid action")

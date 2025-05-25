print("Welcome to contacts manager CLI!")
contacts= []
tags = ("friend", "family", "work", "others")

while True:
    print("\nChoose an option:")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact by Name")
    print("4. Delete Contact by Name")
    print("5. Show All Unique Tags Used")
    print("6. Exit")
    print ("Choose an option: 1 to 5")

    options = int(input())
    if options == 1:
        name = input("Enter name: ") 
        phone = input("Enter phone number: ")
        email = input("Enter your mail: ")
        print("Available tags:", tags)
        tag = input("pick tag from above: ")
        if tag in tags:
            new_contact = {
                "name": name, 
                "phone": phone,
                "email": email,
                "tag": tag
            }
            contacts.append(new_contact)
            print("Contact added successfully")
        else:
            print("Invalid tag. Contact not added.")
    elif (options == 2):
        for contact in contacts:
            print(contact)
    elif(options == 3):
        search_name = input("Input")
        found = False
        for contact in contacts:
            if contact["name"] == search_name:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Tag: {contact['tag']}")
                found = True
        if not found:
            print("No match found")

    elif(options == 4):
        del_name = input("Input")
        found = False
        for contact in contacts:
            if contact["name"] == del_name:
                contacts.remove(contact)
                found = True
        if not found:
            print("Contact not found")
    elif (options == 5):
        tagSet = set()
        for contact in contacts :
            tagSet.add(contact["tag"])
        print(tagSet)
    else:
        print("Invalid Choice. Try again.")
        break


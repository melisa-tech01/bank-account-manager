accounts = {
    "melisa":{
        "password": "1234",
        "balance": 1500,
        "cards": {"Visa", "Mastercard"}
    },
    "lucky": {
        "password": "abcd",
        "balance": 300,
        "cards": {"Debit Card"}
    }
}

def login(username, password):                             
    if username in accounts:
        if password == accounts[username]["password"]:
            return username                                 
        else:
            print("Wrong Password")
    else:
        print("User does not exist")

print("-----Bank Account Manager-----")
print("1. Login\n2. Show balance\n3. Add card\n4. Remove card\n5. Show all customers\n6. Logout")
Auswahl = input("> ")
eingeloggter_user = None
if Auswahl == "1":
    username = input("Whats your username: ")
    password = input("Whats your password: ")
    eingeloggter_user = login(username, password)
    while eingeloggter_user:
           print("-----", "Welcome", eingeloggter_user, "-----")
           print("1. Show balance\n2. Add card\n3. Remove card\n4. Show all customers\n5. Logout")
           Auswahl = input("> ")

           if Auswahl == "1":
               print("Your balance is: ")
               print(accounts[eingeloggter_user]["balance"])

           elif Auswahl == "2":
               new_card = input("Add your card: " )
               accounts[eingeloggter_user]["cards"].add(new_card)
               print("Card added")

           elif Auswahl == "3":
               old_card = input("Which card do you want to remove?: ")
               accounts[eingeloggter_user]["cards"].discard(old_card)
               print("Card removed")

           elif Auswahl == "4":
               for username in accounts:
                   print(username)
                   print(accounts[username])

           elif Auswahl == "5":
               print("Goodbye!")
               eingeloggter_user = None
                   



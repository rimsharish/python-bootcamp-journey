bank = {
    56458: {
        "profile": {
            "username": "irfan",
            "full_name": {
                "first": "Irfan",
                "last": "K"
            },
            "contact": {
                "phone": ["+91-9876543210"],
                "email": ["irfan@example.com"]
            }
        },
        "security": {
            "pin": 8945,
            "login_history": [
                {"date": "2026-06-01", "device": "mobile"},
                {"date": "2026-06-03", "device": "laptop"}
            ]
        },
        "account": {
            "balance": 72000,
            "currency": "INR",
            "linked_cards": [
                {"type": "debit", "last4": "1234"},
                {"type": "credit", "last4": "5678"}
            ]
        },
        "transactions": [
            ["deposit", 5000, "2026-05-30"],
            ["withdraw", 2000, "2026-06-02"]
        ]
    },

     485965: {
        "profile": {
            "username": "alice",
            "full_name": {
                "first": "Alice",
                "last": "Johnson"
            },
            "contact": {
                "phone": ["+91-9123456780"],
                "email": ["alice@example.com"]
            }
        },
        "security": {
            "pin": 8745,
            "login_history": [
                {"date": "2026-06-02", "device": "tablet"},
                {"date": "2026-06-03", "device": "mobile"}
            ]
        },
        "account": {
            "balance": 98000,
            "currency": "INR",
            "linked_cards": [
                {"type": "debit", "last4": "1111"}
            ]
        },
        "transactions": [
            ["deposit", 10000, "2026-06-01"],
            ["transfer", 3000, "2026-06-03"]
        ]
    },

    748596: {
        "profile": {
            "username": "sajwa",
            "full_name": {
                "first": "Sajwa",
                "last": "M"
            },
            "contact": {
                "phone": ["+91-9988776655"],
                "email": ["sajwa@example.com"]
            }
        },
        "security": {
            "pin": 7895,
            "login_history": [
                {"date": "2026-06-01", "device": "desktop"}
            ]
        },
        "account": {
            "balance": 120000,
            "currency": "INR",
            "linked_cards": [
                {"type": "debit", "last4": "2222"},
                {"type": "debit", "last4": "3333"}
            ]
        },
        "transactions": [
            ["withdraw", 7000, "2026-06-02"],
            ["deposit", 15000, "2026-06-03"]
        ]
    }
}


# q1 : print fullname (firstname_lname ) of account number 485965


firstname = bank[485965]["profile"]["full_name"]["first"]
lastname = bank[485965]["profile"]["full_name"]["last"]
print(f"{firstname}_{lastname}")



# q2 : change username 'irfan' to 'irfankpm' of acc number 56458


a = bank[56458]["profile"].update({"username" : "irfankpm"})
print(a)
print(bank[56458]["profile"]["username"])




# q3 : add new email for acc number 748596 , keep old email too , input-email


new_email = input("enter a new email : ")
print(f"new email = {new_email}")
b = bank[748596]["profile"]["contact"]["email"].append(f"{new_email}")
print(b)
print(bank[748596]["profile"]["contact"]["email"])



# q4 : deposit '6000' for acc number 748596, update balance,transaction


c = bank[748596]["transactions"].append(["deposit",6000,"2026-06-05"])
print(c)
print(bank[748596]["transactions"])

d = bank[748596]["account"].update({"balance" : 126000})
print(d)
print(bank[748596]["account"]["balance"])


     
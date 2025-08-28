"""
Implement User Management System
"""

import json

users = {
    "alice": {
        "password": "1234",
        "email": "alice@.com",
        "phone": "010-1234-5678",
        "birthday": "1990-01-01",
        "role" : "admin"
    },
    "bob": {
        "password": "5678",
        "email": "bob@.com",
        "phone": "010-5678-1234",
        "birthday": "1992-02-02",
        "role" : "viewer"
    },
    "charlie": {
        "password": "abcd",
        "email": "charlie@.com",
        "phone": "010-9876-5432",
        "birthday": "1995-03-03",
        "role" : "editor"
    }
}

user = ""

print(json.dumps(users, indent=2, ensure_ascii=False))


while True:
    registreOrLogin = input("Do you want to register or login? (r/l): ").strip().lower()
    if registreOrLogin == 'r':
        new_user = input("Enter new username: ")
        if new_user in users:
            print("Username already exists.")
        else:
            new_password = input("Enter password: ")
            new_email = input("Enter email: ")
            new_phone = input("Enter phone: ")
            while True:
                new_birthday = input("Enter birthday (YYYY-MM-DD): ")
                if len(new_birthday) == 10 and new_birthday[4] == '-' and new_birthday[7] == '-':
                    break
                else:
                    print("Invalid date format. Please use YYYY-MM-DD.")
            while True:
                new_role = input("Enter role (admin/editor/viewer): ")
                if new_role in ["admin", "editor", "viewer"]:
                    break
                else:
                    print("Invalid role. Please enter admin, editor, or viewer.")
            users[new_user] = {
                "password": new_password,
                "email": new_email,
                "phone": new_phone,
                "birthday": new_birthday,
                "role": new_role
            }
            print("Registration successful!")
            print(json.dumps(users, indent=2, ensure_ascii=False))
        
    elif registreOrLogin == 'l':
        user = input("Enter username: ")
        password = input("Enter password: ")
        if user in users and users[user]["password"] == password:
            print(f"Welcome, {user}!")
            if users[user]["role"] == "admin":
                print("You have admin privileges. You can manage all users.")
                while True:
                    action = input("Edit or delete a user? (e/d/none): ").strip().lower()
                    if action == 'e':
                        edit_user = input("Enter the username to edit: ")
                        if edit_user in users:
                            new_email = input("Enter new email: ")
                            new_phone = input("Enter new phone: ")
                            while True:
                                new_birthday = input("Enter new birthday (YYYY-MM-DD): ")
                                if len(new_birthday) == 10 and new_birthday[4] == '-' and new_birthday[7] == '-':
                                    break
                                else:
                                    print("Invalid date format. Please use YYYY-MM-DD.")
                            while True:
                                new_role = input("Enter new role (admin/editor/viewer): ")
                                if new_role in ["admin", "editor", "viewer"]:
                                    break
                                else:
                                    print("Invalid role. Please enter admin, editor, or viewer.")
                            users[edit_user].update({
                                "email": new_email,
                                "phone": new_phone,
                                "birthday": new_birthday,
                                "role": new_role
                            })
                            print(f"User {edit_user} updated successfully.")
                            print(json.dumps(users, indent=2, ensure_ascii=False))
                        else:
                            print("User not found.")
                    elif action == 'd':
                        delete_user = input("Enter the username to delete: ")
                        if delete_user in users:
                            del users[delete_user]
                            print(f"User {delete_user} deleted successfully.")
                            print(json.dumps(users, indent=2, ensure_ascii=False))
                        else:
                            print("User not found.")
                    
            elif users[user]["role"] == "editor":
                print("You have editor privileges.You can manage all users. But cannot delete users.")
                while True:
                    action = input("Edit a user? (e/none): ").strip().lower()
                    if action == 'e':
                        edit_user = input("Enter the username to edit: ")
                        if edit_user in users:
                            new_email = input("Enter new email: ")
                            new_phone = input("Enter new phone: ")
                            while True:
                                new_birthday = input("Enter new birthday (YYYY-MM-DD): ")
                                if len(new_birthday) == 10 and new_birthday[4] == '-' and new_birthday[7] == '-':
                                    break
                                else:
                                    print("Invalid date format. Please use YYYY-MM-DD.")
                            while True:
                                new_role = input("Enter new role (admin/editor/viewer): ")
                                if new_role in ["admin", "editor", "viewer"]:
                                    break
                                else:
                                    print("Invalid role. Please enter admin, editor, or viewer.")
                            users[edit_user].update({
                                "email": new_email,
                                "phone": new_phone,
                                "birthday": new_birthday,
                                "role": new_role
                            })
                            print(f"User {edit_user} updated successfully.")
                            print(json.dumps(users, indent=2, ensure_ascii=False))
                        else:
                            print("User not found.")
            elif users[user]["role"] == "viewer":
                print("You have viewer privileges. You can manage only your own profile.")
                while True:
                    action = input("Edit your profile? (e/none): ").strip().lower()
                    if action == 'e':
                        new_email = input("Enter new email: ")
                        new_phone = input("Enter new phone: ")
                        while True:
                            new_birthday = input("Enter new birthday (YYYY-MM-DD): ")
                            if len(new_birthday) == 10 and new_birthday[4] == '-' and new_birthday[7] == '-':
                                break
                            else:
                                print("Invalid date format. Please use YYYY-MM-DD.")
                        users[user].update({
                            "email": new_email,
                            "phone": new_phone,
                            "birthday": new_birthday
                        })
                        print(f"Your profile updated successfully.")
                        print(json.dumps(users, indent=2, ensure_ascii=False))
        else:
            print("Invalid username or password.")
#-------------------------------------------------
#  رابط شرح الاكواد يوتيوب https://youtu.be/25oeWOWjMVY?si=Tljd6NnVTL072c-l
# --->>>  Final Poject Solution (دليل هواتف)
# --->>>  Presented to: Eng. Ebtisam Dawoud
# --->>>  Deema Mohammed AL-Maqadma
# --->>>  ID : 2320230766
#------------------------------------------------- 

# Class to manage phone book operations
class PhoneBook:
    def __init__(self):
        self.phone_book = []

    # Validate phone number format
    def is_valid_phone(self, phone):
        return phone.startswith("059") and len(phone) == 10 and phone.isdigit()

    # Validate ID number format
    def is_valid_id(self, id_number):
        return len(id_number) == 9 and id_number.isdigit()

    # Add a new phone entry
    def add_phone(self):
        phone = input("---> Enter phone number (059xxxxxxx): ")
        if not self.is_valid_phone(phone):
            print("---> Invalid phone number format!.")
            return

        id_number = input("---> Enter ID number (9 digits): ")
        if not self.is_valid_id(id_number):
            print("---> Invalid ID number.")
            return

        name = input("---> Enter name: ")
        age = input("---> Enter age: ")
        address = input("---> Enter address: ")

        self.phone_book.append({
            "phone": phone,
            "id": id_number,
            "name": name,
            "age": age,
            "address": address
        })
        print("---> Phone number added successfully!")

    # Show all phone entries
    def show_all(self):
        if not self.phone_book:
            print("---> No phone numbers found.")
        else:
            for entry in self.phone_book:
                print(entry)

    # Search for a phone number
    def search_phone(self):
        phone = input("---> Enter phone number to search: ")
        for entry in self.phone_book:
            if entry["phone"] == phone:
                print("Found:", entry)
                return
        print("---> Phone number not found.")

    # Update address of a phone entry
    def update_phone(self):
        phone = input("---> Enter phone number to update: ")
        for entry in self.phone_book:
            if entry["phone"] == phone:
                new_address = input("---> Enter new address: ")
                entry["address"] = new_address
                print("---> Address updated.")
                return
        print("---> Phone number not found.")

    # Delete a phone entry
    def delete_phone(self):
        phone = input("---> Enter phone number to delete: ")
        for entry in self.phone_book:
            if entry["phone"] == phone:
                self.phone_book.remove(entry)
                print("---> Phone number deleted.")
                return
        print("---> Phone number not found.")
#-------------------------------------------------
#  رابط شرح الاكواد يوتيوب https://youtu.be/25oeWOWjMVY?si=Tljd6NnVTL072c-l
# --->>>  Final Poject Solution 
# --->>>  Presented to: Eng. Ebtisam Dawoud
# --->>>  Deema Mohammed AL-Maqadma
# --->>>  ID : 2320230766
#-------------------------------------------------
from PhoneBook import PhoneBook

# Constants for admin credentials
ADMIN_USERNAME = "Deema"
ADMIN_PASSWORD = "2320230766"

# Class to handle user interaction and app flow
class PhoneBookApp:
    def __init__(self):
        self.phone_book = PhoneBook()

    # Admin login verification
    def admin_login(self):
        username = input("---> Enter username: ")
        password = input("---> Enter password: ")
        return username == ADMIN_USERNAME and password == ADMIN_PASSWORD

    # Admin dashboard menu
    def admin_dashboard(self):
        while True:
            print("\n-------> Admin Dashboard <-------\n")
            print("1- Add Phone Number")
            print("2- Show All Phone Numbers")
            print("3- Search Phone Number")
            print("4- Update Phone Data")
            print("5- Delete Phone Number")
            print("6- Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.phone_book.add_phone()
            elif choice == "2":
                self.phone_book.show_all()
            elif choice == "3":
                self.phone_book.search_phone()
            elif choice == "4":
                self.phone_book.update_phone()
            elif choice == "5":
                self.phone_book.delete_phone()
            elif choice == "6":
                break
            else:
                print("---> Invalid choice!")

    # Main menu for the app
    def run(self):
        print("\n*** Welcome, the System is ready now! ***\n")
        while True:
            print("\n1- Admin Dashboard")
            print("2- Search for phone number")
            print("3- Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                if self.admin_login():
                    self.admin_dashboard()
                else:
                    print("---> Wrong username or password!")
            elif choice == "2":
                self.phone_book.search_phone()
            elif choice == "3":
                print("\n***** Thx ^_^ *****\n")
                break
            else:
                print("Invalid choice!")

#---------------------------------------------------------
# Start the application
app = PhoneBookApp()
app.run()
print("\n*** By Deema Mohammed AL-Maqadma ***\n")
                    
                    
                
                    
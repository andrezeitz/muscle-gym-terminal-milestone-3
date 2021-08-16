import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('muscle_gym')


def start_menu():
    """
    Start
    """
    print("Hi. Welcome to Muscle Gym.\n")
    while True:
        user_decide = input("""
        If you are a new customer please press 1.
        If you are a existing customer please press 2.
        If you are staff manager please press 3.
        """)
        if validate_start_menu(user_decide):
            break
    start_menu_new_customer(user_decide)        


def validate_start_menu(values):
    """
    Validate if a number is of 1, 2 or 3
    """
    try:
        if (int(values) < 1 or int(values) > 3):
            raise ValueError(
                f"Please enter a number between 1 and 3, you entered {values}"
            )
    except ValueError as e:
        print(f"Invalid number: {e}, please try again.\n")
        return False

    return True


def start_menu_new_customer(value):
    """
    Check if 1,2 or 3 is pressed from the start menu
    """
    if value == "1":
        data_firstname = input("Please provide us with your first name: ")
        print(f"Your first name is saved as {data_firstname}.\n")

        data_lastname = input("Please provide us with your last name: ")
        print(f"Your last name is saved as {data_lastname}.\n")

        data_adress = input("Please provide us with your adress: ")   
        print(f"Your adress is saved as {data_adress}.\n")

        data_zip = input("Please provide us with your zip-code: ")
        print(f"Your zip-code is saved as {data_zip}.\n")

        data_phone = input("Please provide us with your phone number: ")     
        print(f"Your phone number is saved as {data_phone}.\n")

        data_email = input("Please provide us with your email adress: ")
        print(f"Your email adress is saved as {data_email}.\n")
        
        return add_new_customer()


def add_new_customer():
    """
    Add new customers to Google Sheet
    """
    print("Saving your profil to the database...\n")
    new_customer = SHEET.worksheet("new_customers")
    print("Worksheet updated successfully.")
    main()     


# def start_menu():
#     """
#     Start menu to be able to choose three different commands
#     """
#     print("Hi. Welcome to Muscle Gym.\n")
#     print("If you are a new customer please press 1.\n")
#     print("If you are a existing customer please press 2.\n")
#     print("If you are staff please press 3.\n")

#     number_decision = input("Enter your number here: ")
#     while number_decision not in ["1", "2", "3"]:
#             number_decision = input("Wrong number inserted. Please enter your number again: ")

#     if number_decision == "1":
#         new_customer()
#     elif number_decision == "2":
#         existing_customer()
#     elif number_decision == "3":
#         staff()
                   


# def validate_data(values):


# def new_customer():
#     """
#     New customer can sign up with there information
#     """
#     while True:
#         print("You are about to sign up as a new member.\n")

#         data_firstname = input("Please provide us with your first name: ")
#         print(f"Your first name is {new_customer_data}.\n")

#         data_lastname = input("Please provide us with your last name: ")
#         print(f"Your last name is {new_customer_data}.\n")

#         data_adress = input("Please provide us with your adress: ")   
#         print(f"Your adress is {new_customer_data}.\n")

#         data_zip = input("Please provide us with your zip-code: ")
#         print(f"Your zip-code is {new_customer_data}.\n")

#         data_phone = input("Please provide us with your phone number: ")     
#         print(f"Your phone number is {new_customer_data}.\n")

#         data_email = input("Please provide us with your email adress: ")
#         print(f"Your email adress is {new_customer_data}.\n")

#         new_customer_data = data_info.split(",")

#         if validate_data(new_customer_data):
#             print("Data is valid")
#             print (f"{data_firstname}"), print(f"{data_lastname}"), print(f"{data_adress}"), print(f"{data_zip}"), print(f"{data_phone}"), print(f"{data_email}")
#             break

#         return new_customer_data

   

def main():
    """
    Run all program functions
    """
    start_menu()
    


main()    

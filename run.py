import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    Start menu with 3 options
    """
    print("Hi. Welcome to Muscle Gym.\n")
    while True:
        user_decide = input("""
        If you want to registred as a new customer please press 1.
        If you are a existing customer that want to know how much please press 2.
        If you are staff manager please press 3.
        """)
        if validate_start_menu(user_decide):
            break
    start_menu_new_customer(user_decide)


def validate_start_menu(values):
    """
    Validate if a number is of 1, 2 or 3 and if not will send error message
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


def start_menu_new_customer(values):
    """
    Will let the new customer enter all of there information
    """
    if values == "1":
        new_customer = {}

        data_firstname = input("Please provide us with your first name: ")
        new_customer["firstname"] = data_firstname
        print(f"Your first name is saved as {data_firstname}.\n")

        data_lastname = input("Please provide us with your last name: ")
        new_customer["lastname"] = data_lastname
        print(f"Your last name is saved as {data_lastname}.\n")

        data_address = input("Please provide us with your adress: ")
        new_customer["address"] = data_address
        print(f"Your adress is saved as {data_address}.\n")

        data_zipcode = input("Please provide us with your zip-code: ")
        new_customer["zipcode"] = data_zipcode
        print(f"Your zip-code is saved as {data_zipcode}.\n")

        data_phone = input("Please provide us with your phone number: ")
        new_customer["phone"] = data_phone
        print(f"Your phone number is saved as {data_phone}.\n")

        data_email = input("Please provide us with your email adress: ")
        new_customer["email"] = data_email
        print(f"Your email adress is saved as {data_email}.\n")
        return add_new_customer(new_customer)


def add_new_customer(new_customer):
    """
    Add new customers to Google Sheet
    """
    print("Saving your profil to the database...\n")
    worksheet_to_update = SHEET.worksheet("new_customer")
    worksheet_to_update.append_row([x for x in new_customer.values()])
    print("Worksheet updated successfully.")


def main():
    """
    Run all program functions
    """
    start_menu()

main()
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
        user_decide = input(
        """
        If you want to registred as a new customer please press 1.
        If you want to calculate your BMR please press 2.
        If you are staff manager please press 3.
        """
        )
        if validate_start_menu(user_decide):
            break
    start_menu_new_customer(user_decide)
    start_menu_calculate(user_decide)


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


def start_menu_calculate(values):
    """
    Will let the customer calculate there BMR
    """
    if values == "2":
        age = int(input("Please enter your age: "))
        print(f"Your age is saved as {age}.\n")
        weight = int(input("Please enter your weight: "))
        print(f"Your weight is saved as {weight}.\n")
        height = int(input("Please enter your height: "))
        print(f"Your height is saved as {height}.\n")
        male_female = input("Please enter (M) for male or (F) for female: ")


        #BMR Calculator https://www.thecalculatorsite.com/health/bmr-calculator.php
        if male_female == "M":
            bmr = int((10 * weight) + (6.25 * height) - (5 * age) + 5)
        elif male_female == "F":
            bmr = int((10 * weight) + (6.25 * height) - (5 * age) - 161)
        print("Your BMR is " + str(bmr) + ".")
        return calculate_activity(bmr)


def calculate_activity(bmr):
    """
    Let the customer decide on what activity scale they are on and then calculate there BMR from that
    """
    print(
        """
        1. If you are sedentary (little or no exercise)
        2. If you are lightly active (light exercise or sports 1-3 days/week)
        3. If you are moderately active (moderate exercise 3-5 days/week)
        4. If you are very active (hard exercise 6-7 days/week)
        5. If you are super active (very hard exercise and a physical job)
        """
    )
    activity_level = int(input("Select your activity level (1-5) "))
    if activity_level == 1:
        activity_index = 1.2
    elif activity_level == 2:
        activity_index = 1.375
    elif activity_level == 3:
        activity_index = 1.46
    elif activity_level == 4:
        activity_index = 1.725
    elif activity_level == 5:
        activity_index = 1.9
    calculate_activity_calories = int(bmr * activity_index)
    print("If you want to maintain your correct weight you need " + str(calculate_activity_calories) + " calories a day.")
        


def main():
    """
    Run all program functions
    """
    start_menu()
    values = validate_start_menu
    bmr = start_menu_calculate(values)


main()
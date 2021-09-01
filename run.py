import gspread
from google.oauth2.service_account import Credentials
import re

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
    Start menu with 5 options
    """
    print("Hi. Welcome to Muscle Gym.\n")
    while True:
        user_decide = input(
            """
   If you want to register as a new customer please press 1.
   If you want to calculate the membership price please press 2.
   If you want to calculate your Body Mass Index (BMI) please press 3
   If you want to calculate your Basal Metabolic Rate (BMR) please press 4.
   If you want to exit please press 5
   """
        )
        if validate_start_menu(user_decide):
            break
    start_menu_new_customer(user_decide)
    start_menu_calculate_bmr(user_decide)
    start_menu_calculate_bmi(user_decide)
    start_menu_calculate_membership(user_decide)
    start_menu_exit(user_decide)


def validate_start_menu(values):
    """
    Validate if number is between 1-5, if not will send error message
    """
    try:
        if (int(values) < 1 or int(values) > 5):
            raise ValueError(
                f"Please enter a number between 1 and 5, you entered {values}"
            )
    except ValueError as e:
        print(f"Invalid number: {e}, please try again.\n")
        return False

    return True


# regex from https://www.youtube.com/watch?v=prpqNAsxsfw
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):
    """
    Validate email
    """
    if (re.search(regex, email)):
        print("Valid Email")
        return True
    else:
        print("Invalid Email")
        return False


def start_menu_new_customer(values):
    """
    Will let the new customers to enter their information
    and choose if they want silver or gold membership
    """
    if values == "1":
        new_customer = {}

        while True:
            data_name = input("Please type your full name in all caps:\n")
            if not data_name.isupper():
                print("ERROR, please provide us with your name again in caps")
            else:
                break
        new_customer["firstname"] = data_name
        print(f"Your first name is saved as {data_name}.\n")

        while True:
            try:
                data_phone = int(input("Please type your phone number:\n"))
            except ValueError:
                print("ERROR, please provide us with your phone number again")
                continue
            else:
                break
        new_customer["phone"] = data_phone
        print(f"Your phone number is saved as {data_phone}.\n")

        while True:
            email = input("Please type your email address:\n")
            if check(email):
                break
            else:
                continue
        new_customer["email"] = email
        print(f"Your email adress is saved as {email}.\n")

        print("We have two memberships. Silver (30€) and Gold (50€)")
        while True:
            membership = input("Type gold or silver to choose membership:\n")
            if membership.upper() == "SILVER" or membership.upper() == "GOLD":
                break
            else:
                print("Invalid input. Try again.")
        membership = membership.upper()
        new_customer["membership"] = membership
        print(f"Your membership is saved as {membership}.\n")

        return add_new_customer(new_customer)


def add_new_customer(new_customer):
    """
    Add new customers to Google Sheet
    """
    print("Saving your profil to the database...\n")
    worksheet_to_update = SHEET.worksheet("new_customer")
    worksheet_to_update.append_row([x for x in new_customer.values()])
    print("Membership worksheet updated successfully.\n")
    start_menu()


def start_menu_calculate_membership(values):
    """
    Will take information from google sheet and calculate
    how much the membership cost per day for each member
    """
    if values == "2":
        data = SHEET.worksheet("existing_customer").get_all_values()
        print("Calculate the avarge price each time visiting the gym.\n")
        while True:
            email_membership = input("Enter the email you registered with:\n")
            # use zeitz@gmail.com as sample
            # use maria@gmail.com as sample
            for d in data:

                if email_membership == d[2]:
                    if d[3] == "Gold":
                        p = 50
                    else:
                        p = 30
                    values = d[4:]
                    months = data[0][4:]
                    for i in range(len(values)):
                        price = round(p / int(values[i]), 2)
                        print("Price for each time trained",
                              "in " + months[i] + " was " + str(price) + "€\n")
                    start_menu()
            else:
                print("We have no records of your visit. Please try again.")


def start_menu_calculate_bmr(values):
    """
    Will let the customer calculate there BMR if they engage in no activity
    """
    if values == "4":
        while True:
            try:
                age = int(input("Please enter your age:\n"))
            except ValueError:
                print("ERROR, provide your age again")
                continue
            else:
                break
        print(f"Your age is saved as {age}.\n")
        while True:
            try:
                height = int(input("Please enter your height in (cm):\n"))
            except ValueError:
                print("ERROR, provide your height again")
                continue
            else:
                break
        print(f"Your height is saved as {height}.\n")
        while True:
            try:
                weight = int(input("Please enter your weight in (kg):\n"))
            except ValueError:
                print("ERROR, provide your weight again")
                continue
            else:
                break
        print(f"Your weight is saved as {weight}.\n")
        male_female = "M"
        while True:
            male_female = input("Enter (M) for male or (F) for female:\n")
            if male_female.upper() == "M" or male_female.upper() == "F":
                break
            else:
                print("Invalid input. Try again.")
        male_female = male_female.upper()
        # BMR Calculation formula
        # https://www.thecalculatorsite.com/health/bmr-calculator.php
        if male_female == "M":
            bmr = int((10 * weight) + (6.25 * height) - (5 * age) + 5)
        elif male_female == "F":
            bmr = int((10 * weight) + (6.25 * height) - (5 * age) - 161)
        print("Your BMR is " + str(bmr) + ".\n")
        calculate_activity(bmr)


def calculate_activity(bmr):
    """
    Will let the customer decide what activity scale they are on, then it will
    estimate how many calories for maintaining there current weight
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
    # BMR Calculation formula from
    # https://www.thecalculatorsite.com/health/bmr-calculator.php
    activity_level = 0
    while True:
        try:
            activity_level = int(input("Select your activity level (1-5)\n"))
            if activity_level >= 1 and activity_level <= 5:
                break
            else:
                print("Activity level must be between 1-5. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

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

    activity_calories = int(bmr * activity_index)
    print("Calculating your BMR result...\n")
    print(f"Summary: Your body will burn {bmr} calories each day.\n")
    print(f"To maintain your current weight {activity_calories} calories.\n")
    start_menu()


def start_menu_calculate_bmi(values):
    """
    Will let the customer calculate BMI and
    get a result on what scale they are
    """
    # BMI Calculation formula from
    # https://www.thecalculatorsite.com/health/bmicalculator.php
    if values == "3":
        while True:
            try:
                height = float(input("Enter your height in (meter) (1.XX):\n"))
            except ValueError:
                print("ERROR, provide your height again")
                continue
            else:
                break
        print(f"Your height is saved as {height}.\n")
        while True:
            try:
                weight = int(input("Enter your weight in (kg):\n"))
            except ValueError:
                print("ERROR, provide your weight again")
                continue
            else:
                break
        print(f"Your weight is saved as {weight}.\n")
        # Calculate BMI
        bmi_1 = float((weight / height))
        bmi_2 = float((bmi_1 / height))
        round_bmi = round(bmi_2, 2)
        print("Calculating your BMI result...")
        print(f"Your BMI is {round_bmi}.")

        if round_bmi < 18.5:
            print("BMI of less than 18.5 indicates that you are underweight")
        elif 18.5 <= round_bmi <= 24.9:
            print("BMI of 18.5-24.9 indicates that you are at healthy weight")
        elif 25 <= round_bmi <= 29.9:
            print("BMI of 25-29.9 indicates that you are slightly overweight.")
        elif 30 <= round_bmi <= 34.9:
            print("BMI of over 30 indicates that you are moderately obese")
        elif 35 <= round_bmi <= 39.9:
            print("BMI of over 35 indicates that you are severely obese")
        elif round_bmi > 40:
            print("BMI over 40 indicates that you are very severely obese\n")
        start_menu()


def start_menu_exit(values):
    """
    Exit the system
    """
    if values == "5":
        print("Closing down the system...\n")
    quit()


def main():
    """
    Run all program functions
    """
    start_menu()


main()

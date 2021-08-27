import gspread
import math
from google.oauth2.service_account import Credentials
from pprint import pprint
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
    Start menu with 3 options
    """
    print("Hi. Welcome to Muscle Gym.\n")
    while True:
        user_decide = input(
        """
        If you want to registered as a new customer please press 1.
        If you want to calculate the membership price on how many times you train please press 2.
        If you want to calculate your Body Mass Index (BMI) please press 3
        If you want to calculate your Basal Metabolic Rate (BMR) please press 4.
        If you are staff manager please press 5.
        """
        )
        if validate_start_menu(user_decide):
            break
    start_menu_new_customer(user_decide)
    start_menu_calculate_bmr(user_decide)
    start_menu_calculate_bmi(user_decide)
    start_menu_calculate_membership(user_decide)
    start_menu_manager(user_decide)


def validate_start_menu(values):
    """
    Validate if a number is of 1, 2, 3, 4 or 5 and if not will send error message
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


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check(email):
    if (re.search(regex,email)):
        print("Valid Email")
    else:
        print("Invalid Email")

        
def start_menu_new_customer(values):
    """
    Will let the new customer enter all of there information
    """
    if values == "1":
        new_customer = {}

        while True:
            data_name = input("Please provide us with your name in all caps: ")
            if not data_name.isupper():
                print("ERROR, please provide us with your name again")
            else:
                break
        new_customer["firstname"] = data_name
        print(f"Your first name is saved as {data_name}.\n")

        while True:
            try:
                data_phone = int(input("Please provide us with your phone number: "))
            except ValueError:
                print("ERROR, please provide us with your phone number again")
                continue
            else:
                break
        new_customer["phone"] = data_phone
        print(f"Your phone number is saved as {data_phone}.\n")

        if __name__ == "__main__":
            email = input("Please provide us with your email adress: ")
            check(email)
            new_customer["email"] = email
            print(f"Your email adress is saved as {email}.\n")
            return add_new_customer(new_customer)


def add_new_customer(new_customer):
    """
    Add new customers to Google Sheet
    """
    print("Saving your profil to the database...\n")
    worksheet_to_update = SHEET.worksheet("new_customer")
    worksheet_to_update.append_row([x for x in new_customer.values()])
    print("Worksheet updated successfully.")


def validate_times_week(times_week):
    """
    Validate weeks
    """
    try:
        if (int(times_week) < 1 or int(times_week) > 7):
            raise ValueError(
                f"Please enter a number between 1 and 7, you entered"
            )
    except ValueError as e:
        print(f"Invalid number: {e}, please try again.\n")
        return False

    return True


def start_menu_calculate_membership(values):
    """
    Calculate how much the membership will cost per day
    """
    if values == "2":
        print("We have two memberships. Silver (30€) and Gold (50€)")
        print("Let's see which membership is best suited for you...")
        times_week = int(input("How many times per week are you going to train at our gym? "))
 
        #Calculate per month
        times_month = (times_week * 4)
        calculate_silver = round(30 / times_month, 2)
        calculate_gold = round(50 / times_month, 2)
        print(f"Silver membership will cost you {calculate_silver}€ and gold membership {calculate_gold}€ each time you visit the gym")

        if times_week < 3:
            print(f"Okay, if you only train {times_week} time per week we recommend you to choose the silver membership.")
        elif 2 <= times_week <= 4:
            print(f"Cool, if you train {times_week} times per week we recommend you either the silver or gold membership")
        elif times_week > 5:
            print(f"Wow, if you train as much as {times_week} times we recommend you the gold membership")


def start_menu_calculate_bmr(values):
    """
    Will let the customer calculate there BMR if they engage in no activity for that day
    """
    if values == "4":
        while True:
            try:
                age = int(input("Please enter your age: "))
            except ValueError:
                print("ERROR, provide your age again")
                continue
            else:
                break
        print(f"Your age is saved as {age}.\n")
        while True:
            try:
                height = int(input("Please enter your height in (cm): "))
            except ValueError:
                print("ERROR, provide your height again")
                continue
            else:
                break
        print(f"Your height is saved as {height}.\n")
        while True:
            try:
                weight = int(input("Please enter your weight in (kg): "))
            except ValueError:
                print("ERROR, provide your weight again")
                continue
            else:
                break
        print(f"Your weight is saved as {weight}.\n")
        male_female = input("Please enter (M) for male or (F) for female: ")

        # BMR Calculator I took the formula from https://www.thecalculatorsite.com/health/bmr-calculator.php
        if male_female == "M":
            bmr = int((10 * weight) + (6.25 * height) - (5 * age) + 5)
        elif male_female == "F":
            bmr = int((10 * weight) + (6.25 * height) - (5 * age) - 161)
        print("Your BMR is " + str(bmr) + ".")
        return calculate_activity(bmr)


def validate_activity_level(activity_level):
    """
    Validate weeks
    """
    try:
        if (int(activity_level) < 1 or int(activity_level) > 5):
            raise UnboundLocalError(
                f"Please enter a number between 1 and 5"
            )
    except UnboundLocalError as e:
        print(f"Invalid number: {e}, please try again.\n")
        return False

    return True


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
    # BMR Calculator I took the formula from https://www.thecalculatorsite.com/health/bmr-calculator.php
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
    print("Calculating your BMR result...")
    print(f"Summary: Your body will burn {bmr} each day if you engage in no activity for that day. The estimate for maintaining your current weight (based upon your chosen activity level) is {calculate_activity_calories}. This calculation used the Mifflin - St Jeor equation.")


def start_menu_calculate_bmi(values):
    """
    Will let the customer calculate there BMI
    """
    # BMI Calculator I took the formula from https://www.thecalculatorsite.com/health/bmicalculator.php
    if values == "3":
        while True:
            try:
                height = float(input("Please enter your height in (meter): "))
            except ValueError:
                print("ERROR, provide your height again")
                continue
            else:
                break
        print(f"Your height is saved as {height}.\n")
        while True:
            try:
                weight = int(input("Please enter your weight in (kg): "))
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
            print("A BMI of 18.5 - 24.9 indicates that you are at a healthy weight for your height.")
        elif 25 <= round_bmi <= 29.9:
            print("A BMI of 25 - 29.9 indicates that you are slightly overweight.")
        elif 30 <= round_bmi <= 34.9:
            print("A BMI of over 30 indicates that you are moderately obese")
        elif 35 <= round_bmi <= 39.9:
            print("A BMI of over 35 indicates that you are severely obese")
        elif round_bmi > 40:
            print("A BMI of over 40 indicates that you are very severely obese")        


def start_menu_manager(values):
    """
    Let the staff manager
    """
    if values == "5":
        print("Welcome to the admin portal for staff manager")
        see_new_customers = input("If you would like to see the 5 newest customers press 1")
        if see_new_customers == "1":
            new_customers = SHEET.worksheet("new_customer")


def main():
    """
    Run all program functions
    """
    start_menu()


main()

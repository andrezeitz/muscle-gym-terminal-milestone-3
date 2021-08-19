import gspread
import math
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
        If you want to registered as a new customer please press 1.
        If you want to calculate your Basal Metabolic Rate (BMR) please press 2.
        If you want to calculate your Body Mass Index (BMI) please press 3
        If you want to calculate the membership price on how many times you train please press 4.
        If you are staff manager please press 5.
        """
        )
        if validate_start_menu(user_decide):
            break
    start_menu_new_customer(user_decide)
    start_menu_calculate_bmr(user_decide)
    start_menu_calculate_bmi(user_decide)
    start_menu_calculate_membership(user_decide)


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

        data_zipcode = int(input("Please provide us with your zip-code: "))
        new_customer["zipcode"] = data_zipcode
        print(f"Your zip-code is saved as {data_zipcode}.\n")

        data_phone = int(input("Please provide us with your phone number: "))
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


def start_menu_calculate_bmr(values):
    """
    Will let the customer calculate there BMR if they engage in no activity for that day
    """
    if values == "2":
        age = int(input("Please enter your age: "))
        print(f"Your age is saved as {age}.\n")
        height = int(input("Please enter your height in (cm): "))
        print(f"Your height is saved as {height}.\n")
        weight = int(input("Please enter your weight in (kg): "))
        print(f"Your weight is saved as {weight}.\n")
        male_female = input("Please enter (M) for male or (F) for female: ")

        # BMR Calculator I took the formula from https://www.thecalculatorsite.com/health/bmr-calculator.php
        if male_female == "M":
            bmr = int((10 * weight) + (6.25 * height) - (5 * age) + 5)
        elif male_female == "F":
            bmr = int((10 * weight) + (6.25 * height) - (5 * age) - 161)
        print("Your BMR is " + str(bmr) + ".")
        return calculate_activity(bmr)


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
        height = float(input("Please enter your height in (meter): "))
        print(f"Your height is saved as {height}.\n")
        weight = int(input("Please enter your weight in (kg): "))
        print(f"Your weight is saved as {weight}.\n")
        #Calculate BMI
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


def start_menu_calculate_membership(values):
    """
    Calculate
    """
    if values == "4":
        print("We have two memberships. Silver (30€) and Gold (50€)")
        print("Let's see which membership is best suited for you...")
        times_week = int(input("How many times per week are you going to train at our gym? "))
        #Calculate per month
        times_month = (times_week * 4)
        calculate_silver = round(30 / times_month, 2)
        calculate_gold = round(50 / times_month, 2)
        print(f"Silver membership will cost you {calculate_silver} and gold membership {calculate_gold} each time you visit the gym")

        if times_week < 2:
            print(f"Okay, if you only train {times_week} time per week we recommend you to choose the silver membership.")
        elif 2 <= times_week <= 5:
            print(f"Cool, if you train {times_week} times per week we recommend you either the silver or gold membership")
        elif times_week > 5:
            print(f"Wow, if you train as much as {times_week} we recommend you the gold membership")







def main():
    """
    Run all program functions
    """
    start_menu()
    values = validate_start_menu
    bmr = start_menu_calculate_bmr(values)


main()

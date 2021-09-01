# Muscle Gym Terminal

This app is designed to allow people to registered them self for a membership at Muscle Gym. Customers can also calculate how much the membership will cost per each time they are visiting the gym. There is a BMI calculator to check on what level there BMI is right now. It's also possible to check how many calories they burn each day from a BMR calculator.

[Here is the live version of my project](https://muscle-gym.herokuapp.com/)

## Existing Features

* Start menu
  * Customer will be asked to enter a number between 1 and 5.

There are validations to check firstly that the user only enter a number between 1 and 5.
If they dont they will get a error message and be able to enter a correct number.

![menu](https://user-images.githubusercontent.com/85236391/131645665-999a06b0-9da1-4c8f-aaf8-276dfe510ed5.png)

* Registered as a new member
  * Customers will be able to registered them self with inside the terminal.

The information entered by the customer will be saved to a google sheet called new_customer.
All inputs have validators that check so the customer is entered valid information. If not they will be asked to enter the information again.

![New customers](https://user-images.githubusercontent.com/85236391/131643213-624e13f3-6b47-402b-ad86-b3ac0d507a6f.png)

* Calculate existing customer's membership price
  * Customer is able to calculate how much they pay for each time they visited the gym for the last year.

The information is already saved in a google sheet called exisiting_customer and the program will read from it how many times the customer have trained last year and what type of membership they have. For this I already made 2 accounts to take information from zeitz@gmail.com (Gold) and maria@gmail.com (Silver).
All inputs have validations that check so the customer is entered valid information. If not they will be asked to enter the information again.

![Calculate price](https://user-images.githubusercontent.com/85236391/131643241-abf9ed01-dac1-452f-b06a-8923632d7122.png)

* Calculate your BMI (Body Mass Index)
  * Customer is able to calculate there body type scale with the BMI calculation.

The customer will get back information on how there BMI is right now and also if they are underweight, middleweight or overweight.
All inputs have validations that check so the customer is entered valid information. If not they will be asked to enter the information again.

![BMI](https://user-images.githubusercontent.com/85236391/131643259-279a095c-0686-4fde-b900-c0181b8ff65d.png)

* Calculate your BMR (Basal Metabolic Rate)
  * Customer is able to calculate there daily calorie burn rate with the BMR calculation.

Customer will get information on how many calories they should eat to maintain there current weight based on the information they enter.
All inputs have validations that check so the customer is entered valid information. If not they will be asked to enter the information again.

![BMR1](https://user-images.githubusercontent.com/85236391/131643273-a42f4205-cf2f-4886-98d5-79d17b0c277d.png)
![BMR2](https://user-images.githubusercontent.com/85236391/131643283-34f07376-1500-4d92-98a4-ffb95959befd.png)

* Exit the program
  * Customer is able to exit the program

## Future Features
* Allow members to cancel there membership
* Allow members to pay for there membership in the app
* Collect even more information about the members like address and hometown

## How to Use the app
1. When the app finishes loading read the instructions the first part is the most important as it asks you to choose between 5 different numbers.
2. After choosing the number just follow the instructions as they are on screen
3. After finish the start menu will come back up again. Use 5 to exit the program or use a new number.

## Testing
How I have tested the code:

* The python code has been run through the Python pep8 validation and confirmed there are no problems
* I have also run the code through many cycles adding in different values and checking that the output is as expected.
* All inputs have validation to ensure the customer enter the correct information.
* I have tested both in my local terminal and the Code Institute Heroku terminal

### Bugs

#### Solved Bugs
* I had this problem to get the correct return value on the first bmr function.
![Skärmavbild 2021-08-18 kl  11 48 16](https://user-images.githubusercontent.com/85236391/130408610-ac10886e-c73b-4e8d-87f8-4a26a7f207ed.png)

I fixed it by change the return value inside start_menu_calculate(values) from ”return bmr” to instead use ”return calculate_activity(bmr)” and made the bmr readable inside the new function.

* I had this other problem where I calculated the price per visit wrong. I use this formula first to get the result "price = int(values[i]) * (30 / p)".
The price was getting higher if the customer was training more which it obviously shouldn't be.

![Skärmavbild 2021-08-31 kl  17 47 41](https://user-images.githubusercontent.com/85236391/131539117-3ee75343-e78e-4655-9475-e95898c98103.png)

I fast found out it was not working properly and also wanted to get the price to round up to only 2 decimals, so I decided to use round().
First I was getting errors from the terminal on how I did the calculation.

![Skärmavbild 2021-08-31 kl  17 53 34](https://user-images.githubusercontent.com/85236391/131539688-9f5f0c75-629e-481e-8bc3-f30b34e3ea70.png)

Finally I found out how to make the calculation work properly and could move on with no bugs. (price = round(p / int(values[i]), 2))

### Remaining Bugs
* No bugs remaining

### Validation Testing
* PEP8
  * No errors where returned from PEP8online.com

## Technologies
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [Heroku](https://en.wikipedia.org/wiki/Heroku)
* [PEP8](http://pep8online.com/)
* Python Terminal by Code Institute

## Deployment
1. On the home screen click on create new app button
2. Enter a name for the project and select your region to the correct region
3. On the next screen select settings
4. Go to config vars and click reveal config vars
5. Switch to the program file and where you are keeping your credentials copy these and then on Heroku enter a name for the key and paste the code into the config vars value box and click add
6. Now scroll down to buildPacks and click add build packs
7. First select python and click save changes
8. Click back into build packs and choose node.js and click save again
9. Ensure that the Python build pack is at the top of the list you are able to drag and drop if you need to rearrange
10. Now select deploy
11. From the deployment method select GitHub
12. Then click on connect to Github button that appears
13. Click into the search box and search for the project name
14. Once located select connect
15. Then click deploy branch, this will then be shown in the box below
16. You can the click view to show the app in a browser

The program can be deployed automatically but i have chosen to keep it as a manual deploy.

### Cloning
How to clone this repository.

* On GitHub go to the main page of the Repository.
* Above the list of files click the code button with the drop-down arrow.
* To clone the repository using HTTPS, under "Clone with HTTPS", click on the clipboard.
* Open the Git Bash terminal.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone, and then paste the URL you copied earlier from step 3.
* Press Enter to create your local clone.

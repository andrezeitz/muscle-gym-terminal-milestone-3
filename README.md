# Muscle Gym Terminal

This app is designed to allow people to registred themself for a memebership at Muscle Gym. Customers can also calculate how much the membership will cost per each time they are visiting the gym. There is a BMI calculator to check on what level there BMI is right now. It's also possible to check how many calories they burn each day from a BMR calculator.

## Features
* Registred as a new member
  * Customers will be able to registred themself with inside the terminal.

![Skärmavbild 2021-08-31 kl  18 28 47](https://user-images.githubusercontent.com/85236391/131540742-f5fa1ccd-4947-4dcd-afb8-8203ef09fccf.png)


* Calculate existing customers membership price
  * Customer is able to calculate how much they pay for each time they visited the gym for the last year.

* Calculate your BMI (Body Mass Index)
  * Customer is able to calculate there body type scale

![Skärmavbild 2021-08-31 kl  18 30 19](https://user-images.githubusercontent.com/85236391/131540949-ff390636-3b9b-46d5-a0be-78b52efd80fe.png)

* Calculate your BMR (Basal Metabolic Rate)
  * Customer is able to calculate there daily calories burn rate

![Skärmavbild 2021-08-31 kl  18 31 47](https://user-images.githubusercontent.com/85236391/131541146-2277c4de-6cf6-44bb-a4bd-ad04636737c6.png)

* Exit the program
  * Customer is able to exit the program

There are validators to check firstly that the user only enter a number between 1 and 5.
If they dont they will get a error message and be able to enter a correct number.

## How to Use the app
1. When the app finishes loading read the instructions the first part is the most important as it ask you to choose between 5 different numbers.
2. After choosing the number just follow the instructions as they are on screen
3. After finish the start menu will come back up again. Use 5 to exit the program.

## Testing
How I have tested the code:

* The python code has been run through the Python pep8 validator
* I have also run the code through many cycles adding in different values and checking that the output is as expected.
* All inputs have validators to ensure the customer enter the correct information.

### Bugs
I had this problem to get the correct return value on the first bmr function.
![Skärmavbild 2021-08-18 kl  11 48 16](https://user-images.githubusercontent.com/85236391/130408610-ac10886e-c73b-4e8d-87f8-4a26a7f207ed.png)

I fixed it by change the return value inside start_menu_calculate(values) from ”return bmr” to instead use ”return calculate_activity(bmr)” and made the bmr readable inside the new function.

I had this other problem where I calculated the price per visit wrong. I use this formula first to get the result "price = int(values[i]) * (30 / p)".
The price was getting higher if the customer was traning more which it obviously shouldn't be.

![Skärmavbild 2021-08-31 kl  17 47 41](https://user-images.githubusercontent.com/85236391/131539117-3ee75343-e78e-4655-9475-e95898c98103.png)

I fast found out it was not working properly and also wanted to get the price to round up to only 2 decimals so I decided to use the round().
First I was getting errors from the terminal on how I did the calculation.

![Skärmavbild 2021-08-31 kl  17 53 34](https://user-images.githubusercontent.com/85236391/131539688-9f5f0c75-629e-481e-8bc3-f30b34e3ea70.png)

Finally I found out how to make the calulation work properly and could move on with no bugs.

## Technologies
[Python](https://en.wikipedia.org/wiki/Python_(programming_language))
[Heroku](https://en.wikipedia.org/wiki/Heroku)
[PEP8](http://pep8online.com/)
Python Terminal by Code Institute

## Deployment
1. On the home screen click on the create new app button
2. Enter a name for the project and select your region to the correct region.
3. On the next screen select settings
4. Go to config vars and click reveal config vars
5. Switch to the program file and where you are keeping your credentials copy these and then on heroku enter a name for the key and paste the code into the config vars value box and click add
6. Now scroll down to buildPacks and click add build packs
7. First select python and click save changes
8. Click back into build packs and choose node.js and click save again
9. Ensure that the Python build pack is at the top of the list you are abe to drag and drop if you need to rearrange
10. Now select deploy
11. From the deployment method select GitHub
12. Then click on the connect to github button that appears
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

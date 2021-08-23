# Muscle Gym Terminal

This app is designed to allow people to registred themself for a memebership at Muscle Gym. Customers can also calculate how much the membership will cost per each time they are visiting the gym. There is a BMI calculator to check on what level there BMI is right now. It's also possible to check how many calories they burn each day from a BMR calculator.

# Features
* Registred as a new member
  * Customers will be able to registred themself with inside the terminal.

* Calculate membership price
  * Customer is able to calculate price per traning sessions

* Calculate your BMR (Basal Metabolic Rate)
  * Customer is able to calculate there daily calories burn rate

* Calculate your BMI (Body Mass Index)
  * Customer is able to calculate there body type scale

There are validators to check firstly that the user only enter a number between 1 and 5

# How to Use the app
1. When the app finishes loading read the instructions the first part is the most important as it ask you to choose between 5 different numbers.
2. After choosing the number just follow the instructions as they are on screen
3. If you need to start again simply click on the run app button at the top

# Testing
How I have tested the code:

* The python code has been run through the Python pep8 validator
* I have also run the code through many cycles adding in different values and checking that the output is as expected.

## Bugs
I had this problem to get the correct return value on the first bmr function.
![Skärmavbild 2021-08-18 kl  11 48 16](https://user-images.githubusercontent.com/85236391/130408610-ac10886e-c73b-4e8d-87f8-4a26a7f207ed.png)

I fixed it by change the return value inside start_menu_calculate(values) from ”return bmr” to instead use ”return calculate_activity(bmr)” and made the bmr readable inside the new function.

# Technologies
[Python](https://en.wikipedia.org/wiki/Python_(programming_language)
[Heroku](https://en.wikipedia.org/wiki/Heroku)

# Deployment
1. Ensure all the dependencies are included by adding them to the requirements.txt file by running the following command in the terminal: pip3 freeze > requirements.tx
2. Ensure the project has been fully committed and pushed to git
3. Go to your heroku account, if you don't have one create one
4. On the home screen click on the create new app button
5. Enter a name for the project and select your region to the correct region.
6. On the next screen select settings
7. Go to config vars and click reveal config vars
8. Switch to the program file and where you are keeping your credentials copy these and then on heroku enter a name for the key and paste the code into the config vars value box and click add
9. Now scroll down to buildPacks and click add build packs
10. First select python and click save changes
11. Click back into build packs and choose node.js and click save again
12. Ensure that the Python build pack is at the top of the list you are abe to drag and drop if you need to rearrange
13. Now select deploy
14. From the deployment method select GitHub
15. Then click on the connect to github button that appears
16. Click into the search box and search for the project name
17. Once located select connect
18. Then click deploy branch, this will then be shown in the box below
19. You can the click view to show the app in a browser

The program can be deployed automatically but i have chosen to keep it as a manual deploy so i can ensure that while i am testing and have no intention of adding more to the code currently it is better to deploy it manually meaning returning to the screen and clicking deploy branch each time you want to make any changes.

## Cloning
How to clone this repository.

* On GitHub go to the main page of the Repository.
* Above the list of files click the code button with the drop-down arrow.
* To clone the repository using HTTPS, under "Clone with HTTPS", click on the clipboard.
* Open the Git Bash terminal.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone, and then paste the URL you copied earlier from step 3.
* Press Enter to create your local clone.

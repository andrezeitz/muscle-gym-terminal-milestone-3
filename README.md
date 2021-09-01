# Muscle Gym Terminal

This app is designed to allow people to registered them self for a membership at Muscle Gym. Existing custumers can also calculate the average cost per visit to the gym. They will get a full year statistic depending on what membership they have and how many times they trained each month. There is a BMI calculator to check on what level their BMI is right now. It's also possible to check how many calories they burn each day from a BMR calculator.

[Here is the live version of my project](https://muscle-gym.herokuapp.com/)

[Here is the Google Sheet](https://docs.google.com/spreadsheets/d/1jjdcsYbypGQb7LZ-UuAfCqHO--gd7cCnGHkTBQu8WaA/edit#gid=0)

![Skärmavbild 2021-09-01 kl  11 48 13](https://user-images.githubusercontent.com/85236391/131650534-91c03e9e-d9e9-4ab4-9b1e-9ec23c2fe110.png)

## Existing Features

* Start menu
  * Customer will be asked to type a number between 1 and 5.

There are validations to check firstly that the user only enter a number between 1 and 5.
If they dont they will get a error message and be able to enter a correct number.

![menu](https://user-images.githubusercontent.com/85236391/131645665-999a06b0-9da1-4c8f-aaf8-276dfe510ed5.png)

* Registered as a new member
  * Customers will be able to registered them selfs with inside the terminal.

The information entering by the customer will be saved to a google sheet called new_customer.
All inputs have validators that check so the customer is entered valid information. If not they will be asked to enter the information again.

![meeeember](https://user-images.githubusercontent.com/85236391/131723622-637a72f4-8d39-426c-a58e-796f93df465e.png)

* Calculate existing customer's membership price
  * Customer is able to calculate the avarge price on how many times they visited the gym each month for the last year.

The information is already saved in a google sheet called exisiting_customer and the program will read from it how many times the customer have trained each month and what type of membership they have. Please use one of these test accounts when checking if it is working, zeitz@gmail.com (Gold) and maria@gmail.com (Silver).
All inputs have validations that check so the customer is entered valid information. If not they will be asked to enter the information again.

![priccce](https://user-images.githubusercontent.com/85236391/131723639-1f487e98-7cba-47dc-957a-edf3ddb7c233.png)

* Calculate your BMI (Body Mass Index)
  * Customer is able to calculate their body type scale with the BMI calculation.

The customer will get back information on how their BMI is right now and also if they are underweight, middleweight or overweight.
All inputs have validations that check so the customer is entered valid information. If not they will be asked to enter the information again.

![bmiii](https://user-images.githubusercontent.com/85236391/131723655-a39a4faa-081e-4dbc-bd8c-3b152cb03d08.png)

* Calculate your BMR (Basal Metabolic Rate)
  * Customer is able to calculate their daily calorie burn rate with the BMR calculation.

Customer will get information on how many calories they should eat to maintain their current weight based on the information they enter.
All inputs have validations that check so the customer is entered valid information. If not they will be asked to enter the information again.

![bmrr2](https://user-images.githubusercontent.com/85236391/131723669-9738e9d8-e02d-45df-a233-e79a9aa109cc.png)
![bmrr3](https://user-images.githubusercontent.com/85236391/131723677-b594d66d-8c51-4bd2-b197-adedb3ee280d.png)

* Exit the program
  * Customer is able to exit the program

## Data Model
In the new_members sheet I collect all information the customer entered.

![new menber](https://user-images.githubusercontent.com/85236391/131714986-d5fc3948-b75e-4356-b705-0167dc479fad.png)

In the excisting_customers sheet I put in a summary of data for a year. I decided to store four attributes with fake data just to have something to read from.
I'm aware that in a real world senario it would not look like this and every visit would be tracked but for this education project I did it like a summary.

![month](https://user-images.githubusercontent.com/85236391/131715007-34dca87f-ae39-4718-8ef7-c272dd36a388.png)

## Future Features
* Allow members to cancel their membership
* Allow members to pay for their membership in the app
* Collect even more information about the members like address and hometown

## How to Use the app
1. When the app finishes loading read the instructions the first part is the most important as it asks you to choose between 5 different numbers.
2. After choosing the number just follow the instructions as they are on screen
3. After finish the start menu will come back up again. Use 5 to exit the program or use a new number.

## Testing
How I have tested the code:

* The python code has been run through the Python pep8 validation and confirmed there are no problems
* I have also run the code through many cycles adding in different values and checking that the output is as expected.
* All inputs have validation to ensure the customer enters the correct information.
* I have tested both in my local terminal and my deployed Heroku terminal

### Bugs

#### Solved Bugs
* I had this problem where I calculated the price per visit wrong. I use this formula first to get the result "price = int(values[i]) * (30 / p)".
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

![pep no error](https://user-images.githubusercontent.com/85236391/131722822-d0238811-8835-41ab-8199-d4dbead2cffc.png)

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

## Credits
* [Calculation formula for BMR](https://www.thecalculatorsite.com/health/bmr-calculator.php)
* [Calculation formula for BMI](https://www.thecalculatorsite.com/health/bmicalculator.php)
* [Mail regex validation](https://www.youtube.com/watch?v=prpqNAsxsfw)
* Code Intitute for the deployment terminal

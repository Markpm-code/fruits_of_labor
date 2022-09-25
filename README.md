# Fruits of Labor
Fruits of Labor is Python terminal program, which runs in the Code Institute terminal in Heroku app.

It is a data automation based on a real life data of products of my parents source of income of our family farm but with a fictional numbers.They post the available products in social media and they get the orders.

The program will ask the user to enter their username before inputting available stocks, orders, cancelled orders and then calculate the total products sold and the surplus to end the program.

[Here is the live version of my Fruits of labor data anamation project.](https://fruits-of-labor.herokuapp.com/)

![This is a sreenshot image](./assets/images/python_prog.png)

## Testing username input validation

* If the user entered incorrect input this following will be printed in the terminal:

  * Please enter correct characters not less than 4
  * Please enter characters not more than 10
  * It must be alphabet only

  ![This is a screenshot image](./assets/images/username_validation.png)

## Testing input validation of available_stocks, orders and cancelled orders

If the user entered incorrect data the following will be printed in the terminal:

  * Please enter available stocks ready for orders
  * Data should be 9 numbers,separated by commas
  * Example: 5,10,15,20,25,30,35,40,45

  ![This is a screenshot image](./assets/images/data_validation.png)







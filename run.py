import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fruits_of_labor')


def get_username():
    """
    Asking the user to input a username before running the program.
    Run a while loop  to collect a valid data from the user,
    if invalid, the loop will repeatedly request data until it is valid.
    A hint is printed in the terminal to give a clue to the user.

    """
    while True:
        username = input("Please enter your name to continue: \n")
        if username.isalpha() and (len(username) >= 4 and len(username) <= 10):
            print("Your username is: " + username)  
            break
        else: 
            print("Please enter correct characters not less than 4\n")
            print("Please enter characters not more than 10\n")
            print("It must be alphabet only\n")


def get_available_stocks_data():
    """
    Get available stock data figures input from the user.
    Run a while loop  to collect a valid data from the user,
    if invalid, the loop will repeatedly request data until it is valid.
    An example is printed in the terminal to give a clue to the user.
    """
    while True:
        print("Please enter available stocks ready for orders.\n")
        print("Data should be 9 numbers,separated by commas.\n")
        print("Example: 5,10,15,20,25,30,35,40,45\n")

        stocks_data = input("Enter your available stocks data here: \n")
        available_stocks_data = stocks_data.split(",")

        if validate_data(available_stocks_data):
            print("Data is valid.")
            break    

    return available_stocks_data


def validate_data(values):
    """
    Inside the try, converts all string into integers,
    Raises ValueError if strings cannot be converted into int,
    or if there are not exactly 9 values.
    """   
    try:
        [int(value) for value in values]
        if len(values) != 9:
            raise ValueError(
                f"9 numbers required, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")      
        return False  

    return True     


def update_available_stocks_worksheet(data):
    """
    Update available_stocks worksheet, 
    add new row with list data entered by the user.
    """
    print("Updating available_stocks worksheet...\n")
    available_stocks_worksheet = SHEET.worksheet("available_stocks")
    available_stocks_worksheet.append_row(data)
    print("Available stocks worksheet updated successfully.\n")


def get_orders_data():
    """
    Get orders data figures input from the user.
    Run a while loop  to collect a valid data from the user,
    if invalid, the loop will repeatedly request data until it is valid.
    An example is printed in the terminal to give a clue to the user.
    """
    while True:
        print("Please enter data of new orders.\n")
        print("Data should be 9 numbers,separated by commas.\n")
        print("Example: 5,10,15,20,25,30,35,40,45\n")

        orders_data = input("Enter your new orders data here: \n")
        new_orders_data = orders_data.split(",")

        if validate_orders_data(new_orders_data):
            print("Data is valid.")
            break    

    return new_orders_data


def validate_orders_data(values):
    """
    Inside the try, converts all string into integers,
    Raises ValueError if strings cannot be converted into int,
    or if there are not exactly 9 values.
    """   
    try:
        [int(value) for value in values]
        if len(values) != 9:
            raise ValueError(
                f"9 numbers required, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")      
        return False  

    return True   


def update_orders_worksheet(data):
    """
    Update orders worksheet, 
    add new row with list data entered by the user.
    """
    print("Updating orders worksheet...\n")
    orders_worksheet = SHEET.worksheet("orders")
    orders_worksheet.append_row(data)
    print("Orders worksheet updated successfully.\n")


def get_cancelled_orders_data():
    """
    Get cancelled orders data figures input from the user.
    Run a while loop  to collect a valid data from the user,
    if invalid, the loop will repeatedly request data until it is valid.
    An example is printed in the terminal to give a clue to the user.
    """
    while True:
        print("Please enter cancelled orders data.\n")
        print("Data should be 9 numbers,separated by commas.\n")
        print("Example: 5,10,15,20,25,30,35,40,45\n")

        cancelled_data = input("Enter your cancelled orders data here: \n")
        cancelled_orders_data = cancelled_data.split(",")

        if validate_data(cancelled_orders_data):
            print("Data is valid.")
            break    

    return cancelled_orders_data


def validate_cancelled_orders_data(values):
    """
    Inside the try, converts all string into integers,
    Raises ValueError if strings cannot be converted into int,
    or if there are not exactly 9 values.
    """   
    try:
        [int(value) for value in values]
        if len(values) != 9:
            raise ValueError(
                f"9 numbers required, you entered {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")      
        return False  

    return True  


def update_cancelled_orders_worksheet(data):
    """
    Update cancelled orders worksheet, 
    add new row with list data entered by the user.
    """
    print("Updating cancelled orders worksheet...\n")
    cancelled_orders_worksheet = SHEET.worksheet("cancelled_orders")
    cancelled_orders_worksheet.append_row(data)
    print("Cancelled orders worksheet updated successfully.\n") 


def calculate_total_no_of_products_sold(orders_row):
    """
    Calculating total number of products sold.

    The total number of products sold is the result of the
    orders subtracted from the  cancelled orders. 
    """  
    print("Calculating total number of products sold...\n") 
    cancelled_orders = SHEET.worksheet("cancelled_orders").get_all_values()
    cancelled_orders_row = cancelled_orders[-1]

    total_of_products_sold_data = []
    for orders, cancelled_orders in zip(orders_row, cancelled_orders_row):
        total_of_products_sold = int(orders) - int(cancelled_orders)
        total_of_products_sold_data.append(total_of_products_sold)

    return total_of_products_sold_data 


def update_total_sold_products_worksheet(data):
    """
    Update total products sold,
    Add new row from the calculated result of the
    calculate_total_no_of_products_sold function.
    """
    print("Updating total of products sold worksheet...\n")
    total_sold_products_worksheet = SHEET.worksheet("total_of_products_sold")
    total_sold_products_worksheet.append_row(data)
    print("Total of products sold worksheet updated successfully.\n") 


def calculate_surplus_data(avl_stocks):
    """
    Calculating surplus data.

    The surplus data is the result of available_stocks subtracted to 
    the total of products sold.
    """
    avl_stocks = SHEET.worksheet("available_stocks").get_all_values()
    avl_stocks_row = avl_stocks[-1]
    tops = SHEET.worksheet("total_of_products_sold").get_all_values()
    tops_sold_row = tops[-1]

    surplus_data = []
    for avl_stocks, tops in zip(avl_stocks_row, tops_sold_row):
        surplus = int(avl_stocks) - int(tops)
        surplus_data.append(surplus)
    
    return surplus_data


def update_surplus_worksheet(data):
    """
    Update surplus worksheet,
    Add new row from the calculated result of the
    calculate_surplus_data function.
    """
    print("Updating surplus worksheet...\n")
    surplus_worksheet = SHEET.worksheet("surplus")
    surplus_worksheet.append_row(data)
    print("Surplus worksheet updated successfully.\n")


def main():
    """
    Run all program functions
    """
    get_username()
    data = get_available_stocks_data()
    new_stocks_data = [int(num) for num in data]
    update_available_stocks_worksheet(new_stocks_data)
    data = get_orders_data()
    new_orders_data = [int(num) for num in data]
    update_orders_worksheet(new_orders_data)
    data = get_cancelled_orders_data()
    new_cancelled_orders_data = [int(num) for num in data]
    update_cancelled_orders_worksheet(new_cancelled_orders_data)
    new_total_sold_data = calculate_total_no_of_products_sold(new_orders_data)
    update_total_sold_products_worksheet(new_total_sold_data)
    new_surplus_data = calculate_surplus_data(new_total_sold_data)
    update_surplus_worksheet(new_surplus_data) 


print("Welcome to Fruits of Labor Data Automation")   
main() 

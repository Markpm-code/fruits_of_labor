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
    Asking the user to input a username before 
    running the program.

    """
    while True:
        username = input("Please enter your name to continue: ")
        if username.isalpha() and (len(username) >= 4 and len(username) <= 10):
            print("Your username is: " + username)  
            break
        else: 
            print("Please enter correct characters not less than 4\n")
            print("Please enter characters not more than 10\n")
            print("It must be alphabet only\n")
            continue 


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

        stocks_data = input("Enter your available stocks data here: ")
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

        orders_data = input("Enter your new orders data here: ")
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

        cancelled_data = input("Enter your cancelled orders data here: ")
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


print("Welcome to Fruits of Labor Data Automation")   
main() 

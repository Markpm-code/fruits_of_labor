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


while True:
    username = input("Please enter your name to continue:")

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
    Get available stock data figures input from the user
    """
    print("Please enter available stocks ready for orders.\n")
    print("Data should be 9 numbers,separated by commas.\n")
    print("Example: 5,10,15,20,25,30,35,40,45\n")

    stocks_data = input("Enter your stocks data here: ")

    available_stocks_data = stocks_data.split(",")
    validate_data(available_stocks_data)


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
                f"9 numbers required, you input {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")     
         

get_available_stocks_data()

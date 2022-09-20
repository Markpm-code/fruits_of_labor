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


orders = SHEET.worksheet("orders")

data = orders.get_all_values()

print(data)

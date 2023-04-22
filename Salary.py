# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:29:15 2022

@author: codeolicos
"""

import csv

SHIFT_PAYMENT = 3000
MIN_SALARY = 30000
SALES_THRESHOLD = 20000

def creation():
    
    """ Creates new csv file in order to replace fixed records """
    
    file = open("This_month.csv", "w")
    file.close()
    
def check_number(number, message):
    
    """ Checking input for being a number, makes you making it a number.
                       Returns the number."""
    
    while number.isdecimal() != True:
        print("The input is incorrect, it must be a natural number")
        print(message)
        number = input()
    else:
        return int(number)

def making_shifts():
    
    """ Creating and returning list of lists with shifts from csv file """
    
    file = open("This_month.csv", "r")
    shifts = []
    for shift in file:
        shift = [int(elem) for elem in shift.split(", ")]
        shifts.append(shift)
    file.close()
    return shifts


def daily_bonus(sales):
    
    """ This function takes sales as argument, counts daily bonus
    and return it as a result. """
    
    extra_sales = sales - SALES_THRESHOLD
    
    # For any 1000 of sales above the threshold there is 100 bonus, so I use
    # this formula to round the value
    
    if extra_sales >= 1000:
        bonus = extra_sales // 1000 * 100
    else:
        bonus = 0
        
    return bonus

def shifts_info():
    
    """ Prints numbered list of shifts, numeration starts at 1"""
    
    i = 1
    shifts = making_shifts()
    
    for shift in shifts:
        print(i, shift)
        i += 1
        
def making_record(shift):
    """ Turning shift (list) into a record (string) and appending
        it to file"""
    
    file = open("This_month.csv", "a")
    new_record = str(shift)
    new_record = new_record[1:-1] + "\n"
    file.write(new_record)
    file.close()
    
    # Slice for removing brackets

def recording():
    
    """ Requesting for date and sales, counting bonus, making it a string
    then appending it to file """
    
    
    
    amount_msg = "How many records you want to add? "
    print(amount_msg)
    number = input()
    amount_of_records = check_number(number, amount_msg)
    
       
    
    for i in range(amount_of_records):
        
        
        date_msg = "Enter a date: "
        print(date_msg)
        number = input()
        date = check_number(number, date_msg)
        
        sales_msg = "Enter sales: "
        print(sales_msg)
        number = input()
        sales = check_number(number, sales_msg)
        
        bonus = daily_bonus(sales)
        
        shift = [date, sales, bonus]
        making_record(shift)
        
def check():

    shifts = making_shifts()
    bonus = 0
    days = len(shifts)
    earnings = days * SHIFT_PAYMENT
    
    for i in range(days):
        bonus += shifts[i][2]
        
    total = earnings + bonus
    
    if total > MIN_SALARY:
        salary = total - MIN_SALARY
        prepayment = MIN_SALARY
    else:
        prepayment = total
        salary = 0
        
    print("You worked {0} shifts and earned {1}".format(days, earnings))
    
    print("Also, you get {0} bonus, making it {1} total".format(bonus, 
                                                                total))
    
    print("So, it's {0} as prepayment and {1} as salary".format(prepayment,
                                                                salary))
    
def check_dates():
    
    """ Prints amounts of shifts you've worked, 
    actual dates and statistic """
    
    dates = []
    shifts = making_shifts()
    
    for shift in shifts:
        date = shift[0]
        dates.append(date)
    days = len(dates)
    
        
    print("In this month you had worked {0} days: ".format(days))
    print(*dates)
    shifts_info()
    
def fix():
    
    """ Allowing to choose a shift to change sales number,
    after this function will re-count bonus, make a new record and print
    data of all shifts"""
    
    shifts = making_shifts()
    
    item_msg = "Enter the number of shift you want to fix: "
    print(item_msg)
    numbers_of_records = [str(elem) for elem in range(1, len(shifts) + 1)]
    number = input()
    while number not in numbers_of_records:
        print("Incorrect input")
        print(item_msg)
        number = input()
    else:
        item = int(number)
   
    
    sales_msg = "Enter correct sales: "
    print(sales_msg)
    number = input()
    sales = check_number(number, sales_msg)
    
    shifts[item - 1][1] = sales
    bonus = daily_bonus(sales)
    shifts[item - 1][2] = bonus
    
    # In shift list [1] is position of sales and [2] is position of bonus.
    # Also, I have to subtract 1 from item, since I'm starting 
    # numeration at 1 instead of 0
    
    creation()
    for shift in shifts:
        making_record(shift)
    
    shifts_info()
    print()
    
    print("Enter 1 to fix another record")
    print("Enter 2 to return to main menu")
    print("Enter everything else to exit: \n")
    answer = input()
    
    if answer == "1":
        fix()
    elif answer == "2":
        main()
    else:
        raise SystemExit
    
    
def main():
    
    """ This function runs the program """
    print()
    print("1) Add new shifts")
    print("2) View your salary")
    print("3) View days you've worked")
    print("4) Fix mistake in records")
    selection = input("Make a selection: \n")
    
    if selection == "1":
        recording()
    elif selection == "2":
        shifts_info()
        check()
    elif selection == "3":
        check_dates()
    elif selection == "4":
        shifts_info()
        fix()
    else:
        print("Invalid option, try again")
        main()
    
    
    selection = input(
        "Enter 1 to continue or everything else to finish: \n")
    if selection == "1":
        main()
    else:
        raise SystemExit
        
main()
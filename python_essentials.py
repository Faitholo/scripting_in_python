"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    feb = 28
    leap_feb = feb + 1
    thirty = [4, 6, 9, 11]
    thirty_one = [1, 3, 5, 7, 8, 10, 12]
    if month == 2 and year % 4 == 0:
        return leap_feb
    elif month == 2:
        return feb
    elif month in thirty:
        return 30
    elif month in thirty_one:
        return 31
    else:
        return False
print(days_in_month(2024, 2))


def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    
    
    if year in range(1, 10000) and month in range(1, 13):
        if day >=1:
            if day <= days_in_month(year, month):
                return True
            return False
        return False
    else:
        return False

print(is_valid_date(1993,2,20))


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    


    if is_valid_date(year1, month1, day1) is not False:
        date1 = datetime.date(year1, month1, day1)
        if is_valid_date(year2, month2, day2) is not False:
            date2 = datetime.date(year2, month2, day2)
            date_today = datetime.date.today()
            if date1 < date_today or date2 < date_today:
                if date1 < date2:
                    diff = date2 - date1
                    return diff.days
                return 0
            return 0
        return 0
    return 0
print(days_between(2004, 2, 28, 2004, 6, 4))


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if is_valid_date(year, month, day) is not False:
        birth_date = datetime.date(year, month, day)
        date_today = datetime.date.today()
        if birth_date < date_today:
            diff = date_today - birth_date
            return diff.days
        return 0
    return 0
print(age_in_days(2004, 2, 28))
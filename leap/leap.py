def is_leap_year(year):
    leapYear = False
    if (year % 4 == 0) :
	    if (year % 400 == 0) and year % 100 != 0:
	        leapYear = True
    return leapYear
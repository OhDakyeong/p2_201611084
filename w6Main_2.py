year=raw_input("enter year: ")
year=int(year)
def LeapYear(year):
    if (year%4==0) and (year%100!=0 or year%400==0):
        res="Leap Year"
    else:
        res="Not Leap Year"
    return res
LeapYear(year)
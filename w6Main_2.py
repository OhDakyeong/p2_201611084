"""
@author ODK
@since 160406
"""

year=raw_input("enter year: ")
year=int(year)
def lab6_2(year):
    if (year%4==0) and (year%100!=0 or year%400==0):
        res="Leap Year"
    else:
        res="Not Leap Year"
    print res

def main():
    lab_2()

if __name__=="__main__":
    main()

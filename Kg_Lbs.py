print("Hello, This program converts from kilograms to pounds or pounds to kilograms!")
val1 = ''

while val1 != 'q' and val1 != 'Q':
    val1 = input("Please select your option\n [1] Convert kg-to-LBS\n [2] Convert LBS-to-kg\n [q] to exit \n ")

    #try: Commented try block out due to obsolescence. If implemented again, indent as necessary
    if val1 == '1':  # If user inputs '1', convert kilograms to pounds
        try:
            kg = float(input("Value in kgs that you want to convert to lbs: "))
            lbs = float(kg * 2.205)
            print('The value of {} Kg, is equal to {} lbs'.format(kg, lbs))
        except ValueError:
            print("That's not an numeric!") #Catches when the user enters anything other than a number at conversion
    elif val1 == '2':  # If user inputs '2', convert pounds to kilograms
        try:
            lbs = float(input("Value in lbs that you want to convert to kgs: "))
            kg = float(lbs * 0.4535)
            print('The value of %.2f lbs, is equal to %.2f kg' % (lbs, kg))
        except ValueError:
            print("That's not an numeric!")
    else:
        print("Unknown value...")

    print("\nWould you like to continue?\n")

""" 
    except ValueError:   
        print("Non.....")
"""

print("Thank you, closing the program...") #User has entered 'q', exiting the while loop and stopping the program
exit()

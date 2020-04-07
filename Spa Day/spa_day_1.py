#Name:Zicheng Shi

schedule = [] #get an empty list to store values
def main_menu():
    """ To print out the menu and ask for user selection """
    print "Make a selection:"
    print "1. Add a massage to my schedule"
    print "2. View my current schedule"
    print "3. Cancel a massage from my schedule"
    print "4. Calculate fundraising total"
    print "5. Quit"
    user_selection = int(raw_input("Your selection:")) #get the user_selection using raw_input
    return user_selection #if we didn't return the value, user_selection will only exist in the menu function

def add_function():
    """ To add a schedule. """
    option1 = int(raw_input("Add a (1) 15 minute, (2) 30 minute, or (3) 60 minute massage?"))
    if option1 == 1: #use if statement to append the appointment into my schedule list, however, it would better if we use int to store our appointments
        schedule.append(15)
    elif option1 == 2: # use elif can more precisely get our expected result
        schedule.append(30)
    elif option1 == 3:
        schedule.append(60)
    else:
        print "Add options are 1-3." #this is used to check the error input and print the error message

def review_function():
    """ To view a schedule """
    index1 = 0
    print "Your day contains:"
    while index1 < len(schedule): #use while loop to view our appointments
        print index1,":",schedule[index1],"minute"
        index1 += 1

def cancel_function():
    """ to cancel a schedule """
    if schedule == []: #this if statement is to help us detect the error, if the schedule list is still empty, we cannot delete anything, so we need to print the error message.
        print "Unable to cancel a massage, no massages scheduled."
    else:
        index1 = 0 #firstly use while loop to indicate my schedule
        print "Your day contains:"
        while index1 < len(schedule):
            print index1,":",schedule[index1],"minute"
            index1 += 1
        cancel_choice =int(raw_input( "Which massage do you want to cancel? ")) #get user_choice to cancel a massage
        schedule.pop(cancel_choice) #use pop to delete an element from my list

def calculate_total():
    """ to calculate the total price """
    money_15 = schedule.count(15)*20
    money_30 = schedule.count(30)*30
    money_60 = schedule.count(60)*60
    total = money_15+money_30+money_60 # use list.count() to get how many 15, 30, 60 in my list, and then accordingly times the expenses, finally plus them
    print "Your current total is $"+str(total)


def main_function():
    """ to bring all the functions together """
    print "UW-Madison DPT Massage Fundraiser Scheduler" #this is the first line should print, and would only print for one time.
    user_selection = 0 #cause we want to run the while loop, we need to give user_selection a value, the value is not important, it's just help us to run the function.
    while user_selection != 5: #use while loop, we need to consider that the only condition we need to exit the menu is when user enter "5", so use while user_selection != 5 to loop.
        user_selection = main_menu() #we have got the value of user_selection in the menu function, but Python doesn't know that user_selection == the value, so we need to call the menu function and then give the value a name: user_selection
        if user_selection == 1: #we use if and elif statements to get our appropriately menu
            add_function()
            print ""
        elif user_selection == 2:
            review_function()
            print ""
        elif user_selection == 3:
            cancel_function()
            print ""
        elif user_selection == 4:
            calculate_total()
            print ""
        elif user_selection == 5: #if the user enters 5, we need to exit this function
            print "Goodbye!"
        else:
            print "Menu options are 1-5." #if user_selection is not in range(1,6), we need to tell them they're wrong and return to the menu to re-start.
            print ""
main_function() # call the main_function to run my program

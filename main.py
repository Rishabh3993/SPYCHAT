# we import some variable from spy_details.py
from spy_details import spy_name, spy_age, spy_salutation, spy_rating, spy_online

# implementing list
status_message_list=['My name is Mr. ABCD', 'Shaken, not stirred', 'Enf of life']

# implementing empty list
friend_name = []
friend_age = []
friend_rating = []
friend_online = []

print'WELCOME SPY!'
# backslash is used  for ignoring that next character
print 'Let\'s get started with your profile'

# making of option to the user
question_continue_or_not='Do you want to continue as '+spy_salutation+''+spy_name+'(Y/N)'
existing=raw_input(question_continue_or_not)

# creating function for status adding , variables: add_status(to add new), current_status( for showing current)
def add_status(current_status):
    updated_status=None

    if current_status!=None:
        print'Your current status is %s \n' %(current_status)
    else:
        print"You don't have any status"

    default=raw_input("Do you want to select from previous status(Y/N)? :")

    if default.upper()=='N':
        new_status=raw_input('which status you want to set ? :')

        if len(new_status)>0:
            status_message_list.append(new_status)
            updated_status=new_status

    elif default.upper()=='Y':
        serial_number=1

        for message in status_message_list:
            print '%d.%s'%(serial_number,message)
            serial_number=serial_number+1

        message_selection=int(raw_input('\n Choose from the status list : '))

        if len(status_message_list)>=message_selection:
            updated_status=status_message_list[message_selection-1]

    else:
        print 'Please select the valid option (Y/N) :'

    if updated_status:
        print'Your updated status is:%s'%(updated_status)

    else:
        print'You not updated your status'

    return updated_status

def add_friend():
    new_name=raw_input('Please enter others Spy friend name :')
    new_salutation=raw_input("Please enter salutation of your spy friend :")
    new_age=int(raw_input('Enter age of spy friend :'))
    new_rating=float(raw_input('Enter the rating :'))


    if len(new_name)>0 and new_age>12 and new_age<50 and new_rating>=spy_rating:
        friend_name.append(new_name)
        friend_age.append(new_age)
        friend_rating.append(new_rating)
        friend_online.append(True)
        print('Spy Friend Added!')

    else:
        print('Sorry!Please try to add a valid spy with proper details')

    return len(friend_name)






# creating function
def start_chat(spy_name,spy_age,spy_rating):
    current_status_message = None



    if spy_age >12 and spy_age <50:

        # we use Placeholder here %s for string , %d for integer and %f for float
        print'Process completed.Welcome' +spy_name+' Age: %d and Rating of:%.2f.Welcome to spyChat' % (spy_age, spy_rating)

        show_menu = True

        while show_menu:
            menu_choices='Please select the option \n 1. Add a status to update \n 2. Add a friend \n ' \
                        '3. Send Secret Message \n 4.Read a secret Message \n 5. Read chat from user \n ' \
                        '6. Close Application \n >'
            menu_choice=raw_input(menu_choices)

            if len(menu_choice)>0:
                menu_choice=int(menu_choice)

                if menu_choice==1:
                   current_status_message=add_status(current_status_message)
                elif menu_choice==2:
                    number_of_friend_list=add_friend()
                    print 'You have %d friends'%(number_of_friend_list)

                else:
                    show_menu=False
    else:
        print 'Your age is not valid to be a spy'

if existing=='Y':
    start_chat(spy_name,spy_age,spy_rating)

else:

    #spy_name is variable and raw_input is method to input the value in variable which is given by user
    spy_name=raw_input('Welcome to spy chat, tell me your spy name first:')

    if len(spy_name)>0:


        spy_salutation=raw_input('Should i call you Mr. or Ms. ?')

        # when we again declare the same variable it overload that value and show to us
        # when we use space between single quote like ' ' then space is also count as string
        spy_name=spy_salutation+' '+spy_name
        #  +  is used for joining(string concatenation) to string
        print'Welome ' + spy_name + '.Glad to see you again!'


        # now we add more information by making some variables
        # we use int(raw_input()) to convert the string into integer directly
        spy_age=int(raw_input('Enter your age:'))

        # we can use and / == to compare two things
        if spy_age>12 and spy_age<50:
            spy_rating=float(raw_input('Enter your spy rating:'))

            # for cases we use if elif(use in making of many cases) and finally else
            if (spy_rating>4.5):
                print'You are awesome spy'
            elif (spy_rating>3.5 and spy_rating<=4.5):
                print 'You are good spy '
            elif (spy_rating>=2.5 and spy_rating<=3.5):
                print 'You can do better'
            else:
                print'We can use somebody to help in office'

            # Making spy online after getting details
            spy_online=True



        else:
            print'Sorry for inconvenience , but your age is not valid'

        start_chat(spy_name, spy_age, spy_rating)

    else:
        print'Please enter your name and try again.'

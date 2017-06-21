from spy_details import spy_name,spy_age,spy_salutation,spy_rating,spy_online

print 'WELCOME SPY!'

# backslash is used  for ignoring that next character
print 'Let\'s get started with your profile'

#making of option to the user
question_continue_or_not='Do you want to continue as '+spy_salutation+''+spy_name+'(Y/N)'
existing=raw_input(question_continue_or_not)

#creating function
def start_chat(spy_name,spy_age,spy_rating):
    current_status_message = None

    spy_name = spy_salutation +''+spy_name

    if spy_age >12 and spy_age <50:
        print'Process completed.Welcome %s Age: %d and Rating of:%f.Welcome to spyChat' % (spy_name, spy_age, spy_rating)

        show_menu = True

        while show_menu:
            menu_choices='Please select the option \n 1. Add a status to update \n 2. Add a friend \n ' \
                        '3. Send Secret Message \n 4.Read a secret Message \n 5. Read chat from user \n ' \
                        '6. Close Application'
            menu_choice=raw_input(menu_choices)

            if len(menu_choice)>0:
                menu_choice=int(menu_choice)

                if menu_choice==1:
                    print'you choose to update the status'
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
        #  +  is used for joining(string concatenation) to string
        print'Welome '+spy_name+'.Glad to see you again!'

        spy_salutation=raw_input('Should i call you Mr. or Ms. ?')

        # when we again declare the same variable it overload that value and show to us
        # when we use space between single quote like ' ' then space is also count as string
        spy_name=spy_salutation+' '+spy_name

        # we can write string between " " and ' ' , it will always show output.
        print 'Good work ' +spy_name+ ".I'd like to know a more about you before we proceed."

        #now we add more information by making some variables
        #we use int(raw_input()) to convert the string into integer directly
        spy_age=int(raw_input('Enter your age:'))

        #we can use and / == to compare two things
        if spy_age>12 and spy_age<50:
            spy_rating=float(raw_input('Enter your spy rating:'))

            #for cases we use if elif(use in making of many cases) and finally else
            if spy_rating>4.5:
                print'You are awesome spy'
            elif spy_rating>3.5 == spy_rating<=4.5:
                print 'You are good spy '
            elif spy_rating>=2.5 and spy_rating<=3.5:
                print 'You can do better'
            else:
                print'We can use somebody to help in office'

            #Making spy online after getting details
            spy_online=True

            #printing final statement
            # we use Placeholder here %s for string , %d for integer and %f for float
            print'Process completed.Welcome %s Age: %d and Rating of:%f ..Welcome to spyChat' %(spy_name,spy_age,spy_rating)


        else:
            print'Sorry for inconvenience , but your age is not valid'

        start_chat(spy_name, spy_age, spy_rating)

    else:
        print'Please enter your name and try again.'

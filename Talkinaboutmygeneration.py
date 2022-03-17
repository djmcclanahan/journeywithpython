while True: #Creating an infinite loop
    print('Hi! What year were you born?') #Asking user for their birthyear
    birthyear = int(input()) #declaring birthyear as an interger type variable and assigning it the value of whatever the user inputs, hopefully they use numbers
    if birthyear < 1883: #Using operators to determine which generation they fall in based on their input birthyear and data from Wikipedia
        print ('You are a miracle, possibly immortal.') #stating the facts
    elif birthyear < 1901: #if the above statement was true, the program won't get to this point so I don't have to specify a value for the low side of the year range
        print ('You are the Lost Generation.')
    elif birthyear < 1928:
        print('You are the Greatest Generation')
    elif birthyear < 1946:
        print('You are the Silent generation.')
    elif birthyear < 1965:
        print ('You are a Baby Boomer.')
    elif birthyear < 1981:
        print ('You are Generation X.')
    elif birthyear < 1997:
        print ('You are a Millenial.')
    elif birthyear < 2012:
        print ('You are Generation Z.')
    elif birthyear < 2023:
        print ('You are a Generation Alpha.')
    elif birthyear < 9998:
        print ('You are from the future.')
    elif birthyear == 9999 : # Added a "code" that allows the program to end the infinite loop
            break # this actually breaks the loop and ends the sequence
print(' Thank you, Goodbye') #Machines should be polite too

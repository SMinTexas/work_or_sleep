#The user will enter a number between 0 and 6 inclusive and given
#this number, will make a decision as to whether to sleep in or
#go to work depending on the day of the week.  Day = 0 - 4 go to work
#Day = 5-6 sleep in

day = int(input('Day (0-6)? '))

if day >= 5 and day < 7:
    print('Sleep in')
elif day >= 0 and day <= 4:
    print('Go to work')
else:
    print('You are outside the range of available days of the week!')
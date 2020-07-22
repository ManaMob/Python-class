Num = int(input('Type number of a year:'))
if Num % 4 != 0:
    print('not a leap year')
elif Num % 4 == 0 and Num % 400 == 0:
    
     print('a leap year')
elif Num % 4 == 0 and Num % 100 == 0:
    
     print(' not a leap year')

elif Num % 4 == 0:
    print('a leap year')

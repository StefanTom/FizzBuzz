#For loop that's range starts at 1 and ends at 100
for num in range(1,101):

# if statement that checks if looped number is divisible by 3 and 5 by dividing and comparing to zero
    if num % 3 == 0 and num % 5 == 0:
        fbval = 'FizzBuzz'
        
# elif statement that checks if looped number is divisible by 3 by dividing and comparing to zero
    elif num % 3 == 0:
        fbval = 'Fizz'

# elif statement that checks if looped number is divisible by 5 by dividing and comparing to zero
    elif num % 5 == 0:
        fbval = 'Buzz'

# else prints off all other numbers that don't fit parameters
    else:
        fbval = num
    print(fbval)
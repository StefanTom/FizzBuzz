for x in range(1,101):
    if x % 3 == 0 and x % 5 == 0:
        fbval = 'FizzBuzz'
    elif x % 3 == 0:
        fbval = 'Fizz'
    elif x % 5 == 0:
        fbval = 'Buzz'
    else:
        fbval = x
    print(fbval)
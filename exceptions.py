try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError as ex:
    print(ex, 'That was not a natural number so I do not know what to do.')
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')
except: # this generic except: can only go last
    print("Something strange has happened here... Sorry!")
finally:
    print("Finally there is nothing more to do")

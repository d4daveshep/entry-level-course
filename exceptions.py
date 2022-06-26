try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError as ex:
    print(ex, 'That was not a natural number so I do not know what to do.')
    print(ex.__str__())
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')
except: # this generic except: can only go last
    print("Something strange has happened here... Sorry!")
else:
    print("The else block is run only if there was no exception raised")

finally:
    print("Finally there is nothing more to do")
    print("Finally block is run regardless of exception raise or not - it its always run")

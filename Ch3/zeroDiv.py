# Beginning of the end.
# I'm embarking on my journey to learn Python
# These comments will always be in the beginning of my programs
# Enjoy, Golgothus
# https://github.com/Golgothus
# Ch. 3 Functions

def spam(divBy):
    try:
        div = 42 / int(divBy)
        print(int(div))
    except ZeroDivisionError:
        print('Error: Cannot divide by 0, please use a different number .')
    except TypeError:
        print('Please insert a number.')
    except ValueError:
        print('Please insert a number.')

message = ''

while message != 'No.':
    userInput = ''
    print('Type a number to divide it by 42.')
    userInput = input()
    spam(userInput)
    print('Would you like to continue? If not, please enter \'No.\'')
    message = input()

#! /usr/bin/python3

# tuples are made using () not []

print('an example of a tuple is as follows:')
print('(\'banana\',\'eggs\',\'potato\').')
print('an example of a list is as follows:')
print('[\'banana\',\'eggs\',\'potato\'].')

exampleTuple = ('eggs','potato')
exampleList = ['eggs','potato']

type(exampleTuple)
type(exampleList)

# Reference to magic methods and iteration of variables
# https://www.freecodecamp.org/news/int-object-is-not-iterable-python-error-solved/

print('Output the magic methods available for Tuple data types:')
print(dir(exampleTuple))
print('Output the magic methods avialable for List data types:')
print(dir(exampleList))
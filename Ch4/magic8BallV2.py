#! /usr/bin/python3

import random

# indentation in lists does not matter
# Python will read the values normally
messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(len(messages))
print(messages[random.randint(0, len(messages) - 1)])
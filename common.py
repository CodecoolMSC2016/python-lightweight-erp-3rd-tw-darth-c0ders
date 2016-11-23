# implement commonly used functions here

import random


# generate and return a unique and random string
# other expectation:
# - at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter
# - it must be unique in the list
#
# @table: list of list
# @generated: string - generated random string (unique in the @table)
def generate():
    
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    special = '<>#&@{}<>^!%/=:_'
    number = '1234567890'

    generated = random.choice(lower) + random.choice(upper) + random.choice(number) + random.choice(number) + random.choice(lower) + random.choice(upper) + '#&'

    return generated

def generate_random(table):

    generated = generate()
    while generated in table:
        generated = generate()
    
    return generate

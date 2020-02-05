""" Factorial function, defined recursively. Taken from pg 51 from Introduction
to Computation and Programming Using Python by John Guttag

Assumes that n is an int >= 0"""

def factR(n):
    if n == 0:
        return 1
    else:
        return n * factR(n-1)

print('Welcome to the Factorial Calculator!')
n = int(input('Enter an int >= 0.'))
print(factR(n))

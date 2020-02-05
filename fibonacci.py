"""Fibonacci calculator from pg 58 of Introduction to Computation
and Programming Using Python by John Guttag. Contains a global variable
to count recursive calls to Fibonacci function."""

def fib(x):
    """Assumes x is an int >= 0!!!"""
    global numFibCalls
    numFibCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

def testFib(n):
    for i in range(n+1):
        global numFibCalls
        numFibCalls = 0
        print('fib of', i, '=', fib(i))
        print('fib called', numFibCalls, 'times. \n')

print('Welcome to the Fibonacci Number Calculator!')
n = int(input('''Enter an int >= 0 (called n), and the calculator
will print up to the nth Fibonacci number. '''))
testFib(n)        

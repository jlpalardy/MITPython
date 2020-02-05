#Simple bisection search program to find the square root of a
#nonnegative number. Used pg 33 of 'Introduction to Computation and
#Programming Using Python by John Guttag as a reference.

print('Hello! Welcome to the square root calculator (v1).')

x = float(input('Enter a non-negative number, please.'))
epsilon = .01 #Error term
numGuesses = 0
#Since low's first value is 0 and high is min 1, if a negative number is entered,
#the program runs forever as it tries to find roots
#in narrower and narrower ranges in (0,1). Of course, the roots of negative
#numbers won't be found in Re(0,1).
low = 0.0 #Note low and high are set as floats!
high = max(1.0, x) #1.0 is to account for x's less than 1
ans = (low + high)/2.0

while abs(ans**2 - x) >= epsilon:
          print('low =', low, 'high =', high, 'ans =', ans)
          numGuesses += 1

          if ans**2 < x:
              low = ans
          else:
              high = ans

          ans = (low + high)/2.0

print('number of guesses:', numGuesses)
print(ans, 'is close to the square root of', x)

          



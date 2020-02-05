#Simple bisection search program to find the cube root of a
#nonnegative number. Used pg 33 of 'Introduction to Computation and
#Programming Using Python by John Guttag as a reference.

print('Hello! Welcome to the cube root calculator.')

x = float(input('Enter a real number, please.'))
epsilon = .01
numGuesses = 0
low = min(0.0, x) #The x possibility here is to make the program
#work for neg. numbers
high = max(1.0, abs(x)) #1.0 is to account for x's less than 1
ans = (low + high)/2.0

while abs(ans**3 - x) >= epsilon:
          print('low =', low, 'high =', high, 'ans =', ans)
          numGuesses += 1

          if ans**3 < x:
              low = ans
          else:
              high = ans

          ans = (low + high)/2.0

print('number of guesses:', numGuesses)
print(ans, 'is close to the cube root of', x)

          



# Guess and Check Code Example
cube = 8
for guess in range(cube + 1):
    if guess ** 3 == cube:
        print("Cube root of", cube, "is", guess)
# falls a bit flat when you have an item that doesn't have a perfect cube. Here's a better version:
for guess in range(abs(cube) + 1):
    if guess ** 3 >= abs(cube):
        break
if guess ** 3 != abs(cube):
    print(cube, "is not a perfect cube!")
else:
    if cube < 0:
        guess = -guess
    print("Cube root of " + str(cube) + ' is ' + str(guess))
# Adds the ability to tell the user that the value isn't a perfect cube, also allows us to find the cube
# root of a negative number.

# Approximate solution code
cube = 27
epsilon = 0.1
guess = 0.0
increment = 0.0001
num_guesses = 0

while abs(guess ** 3 - cube) >= epsilon:
    # the above line is pretty clever - the thing inside the abs is the difference between your
    # guess and the actual answer. if it's greater than or equal to epsilon, which is our "too far away"
    # number, we're going to increment our guess by a little, and try again until it's not too far away.
    guess += increment
    num_guesses += 1
print('num_guesses = ', num_guesses)
if abs(guess ** 3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, "is close to the cube root of", cube)


# Bisection search code
cube = 10000
epsilon = .01
num_guesses = 0
low = 0
high = cube
guess = (high + low) / 2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

def bisection(cube, epsilon):
    """
    Given a cube, an error term (epsilon) and a low value, this function will find the cube root of cube.
    :param cube:
    :param epsilon:
    :return:
    """
    low = 0
    high = cube
    guess = (high + low) / 2.0
    num_guesses = 0
    while abs(guess ** 3 - cube) >= epsilon:
        if guess ** 3 < cube:
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
        num_guesses += 1
    print('num_guesses =', num_guesses)
    print(guess, 'is close to the cube root of', cube)


cube = int(input("Enter a number you'd like to find the cube root of: "))
epsilon = float(input("Enter your margin of error: "))
bisection(cube, epsilon)

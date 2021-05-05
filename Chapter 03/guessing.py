## The first code is for you guessing...

# This is code for picking a number. You don't need
# to understand it but can just go to the loop below.
from numpy.random import randint
def input_integer(prompt):
    while True:
        try:
            inp = input(prompt)
            i = int(inp)
            return i
        except Exception:
            print(inp, "is not a valid integer.")

# When picking a random number, we specify the interval
# [low,high). Since high is not included in the interval, 
# we need to use 1 to 21 to get a random number in the
# interval [1,20].
n = randint(1, 21, size = 1)
guess = input_integer("Make a guess> ")
while guess != n:
    if guess > n:
        print("Your guess is too high!")
    else:
        print("Your guess is too low!")
    guess = input_integer("Make a guess> ")
print("You got it!")


## The second part is for the computer guessing.

# This is code for picking a choice. You don't need
# to understand it but can just go to the loop below.
def input_selection(prompt, options):
    """Get user input, restrict it to fixed options."""
    modified_prompt = "{} [{}]: ".format(
        prompt.strip(), ", ".join(options)
    )
    while True:
        inp = input(modified_prompt)
        if inp in options:
            return inp
        # nope, not a valid answer...
        print("Invalid choice! Must be in [{}]".format(
            ", ".join(options)
        ))

for guess in range(1,21):
    result = input_selection(
        "How is my guess {}?".format(guess),
        ["low", "hit", "high"]
    )
    if result == "hit":
        print("Wuhuu!")
        break
    else:
        print("I must have been too low, right?", result)
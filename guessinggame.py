import random 
import math 
# taking upper bound
upper= int(input("Enter upper bound:"))

# taking lower bound
lower= int(input("Enter lower bound:"))

x = random.randint(lower, upper)
print("\n You have only", 
       round(math.log(upper - lower + 1, 2),
        "\n Chances to guess the integer"))

#initialising the number of (counts) guesses

count = 0
#calculation of minimum number of guesses depends on the range
while count < math.log(upper - lower + 1, 2):
    count += 1
    # taking the guess number
    guess = int(input("GUess a number:"))

    if x==count:
        print ("Congratulations you did it in", 
               count, "try(ies)")
        break
    elif x > guess:
        print ("Your guess is too small")
    elif x < guess:
        print ("Your guess is too high")

# if number guesses is more than required
if count >= math.log(upper - lower + 1, 2):
    print("\n The number is %d" % x )
    print("\t Better Luck next time!")


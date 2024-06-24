 ## Assignment - Write a simple program that generate randomly, a series of number, of 10 digits
# ## Note: Start the series integer 4.

import random
rando_code = 4
rando_num = "4" + str(random.randrange(000000000,999999999))
print(f"Account Number Generated Successfully: {rando_num}")

## Guessing Game: 
while True:
    radom_guess = input("Enter your rando between 5 - 10: ")
    comp_guess = random.randrange(5,10)
    if radom_guess == comp_guess:
        print(f"yOU GERRIT, computer guessed {comp_guess}")
        break
    else:
        print(f"You missit, computer guessed {comp_guess}")

# dice roll simulator for food choice 
import random

# create function called roll dice
def roll_dice():
    #return random number 1 through 6
    return random.randint(1, 6)

#create the main function of simulator
def main():
    print("Dice Roll Simulator")

    while True:
        input("Press Enter to roll the dice...")

        dice_roll = roll_dice()
        print("You rolled:", dice_roll)

        #each dice roll number is assigned to the food choice of user
        dice_roll_1 = "Chinese"
        dice_roll_2 = "American"
        dice_roll_3 = "Thai"
        dice_roll_4 = "Mexican"
        dice_roll_5 = "Italian"
        dice_roll_6 = "Indian"

        #printing the assigned dice roll number to the statements above
        if dice_roll == 1:
            print("Food choice:", dice_roll_1)
        elif dice_roll == 2:
            print("Food choice:", dice_roll_2)
        elif dice_roll == 3:
            print("Food choice:", dice_roll_3)
        elif dice_roll == 4:
            print("Food choice:", dice_roll_4)
        elif dice_roll == 5:
            print("Foood choice:", dice_roll_5)
        elif dice_roll == 6:
            print("Food choice:", dice_roll_6)

        #play again yes or no
        play_again = input("Roll again? (y/n): ").lower()
        if play_again != "y":
            break

    print("Thanks for playing!")

#calling the main function
if __name__ == "__main__":
    main()
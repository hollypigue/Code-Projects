#mad libs game

import random
print("Welcome to the Mad Libs Game!")

def mad_libs():
    female_name = input("Enter in a female name: ")
    male_name = input("Enter in a male name: ")
    town_location = input("Enter in a town location: ")
    year = int(input("Enter a year: "))

    story = f"Once upon a time in a land far far away..."
    
    print("\nHere is your own Mad Libs Story: \n")
    print(story)

if __name__ == "__main__":
    mad_libs()
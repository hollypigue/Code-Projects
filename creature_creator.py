#creature creator program
import random

#generate hybrid from input of user of creature1 and creature2
def generate_hybrid_creature(creature1, creature2):
    hybrid_creature = combine_names(creature1, creature2)
    hybrid_creature_stats = generate_stats()
    display_graphic_hybrid(hybrid_creature)
    return hybrid_creature, hybrid_creature_stats

#combine the names the user inputs
def combine_names(name1, name2):
    hybrid_creature = name1[:len(name1)//2] + name2[len(name2)//2:]
    return hybrid_creature

#generate stats of the hybrid from input of user
def generate_stats():
    weight = random.randint(100, 2500)
    diet = random.choice(["plants", "meat", "fish"])
    stats = {"Weight": weight, "Diet": diet}
    return stats 

#display the results and characteristics of creature
def display_graphic_hybrid(hybrid_creature):
    print("Hybrid Creature Generated:\n")
    print(f"Name:  {hybrid_creature}")
    print("=======================================")
    print("              /\______/\     ")
    print("             / ~      ~ \    ")
    print("            /  O      O  \   ")
    print("            \     oo     /   ")
    print("             \  \/\/\/  /    ")
    print("              \________/     ")
    print("=======================================")

#welcome user to the game and to follow the prompts
print("Welcome To The Creature Generating Game!")

#setting creature1 and creature2 to the input of the user
creature1 = input("Enter First Creature: \n")
creature2 = input("Enter Second Creature: \n")

#display the hybrid creatures data
hybrid_creature, hybrid_stats = generate_hybrid_creature(creature1, creature2)
print("Creature Information:")
print(f"Name: {hybrid_creature}")
print("Statistics:")
for stat, value in hybrid_stats.items():
    print(f"{stat}: {value}")
#Always Sunny Character Personality Quiz :)
print("Welcome to the Personality Quiz to see which Always Sunny Character you are!")
print("There will be only yes and no questions to this quiz you will enter 'y' for yes and 'n' for no.")
score = 0

def ask_question(question):
    global score
    answer = input(question + "(y/n): ").lower().strip()
    if answer == 'y':
        score += 1
    elif answer == 'n':
        score-= 1

ask_question("Are you the leader in your group?")
ask_question("Are you a followering in your group?")
ask_question("Do you feel like you are the wildcard in your group")
ask_question("Do you enjoy manipulating people?")
ask_question("Is your dad in jail?")
ask_question("Do people call you a bird?")
ask_question("Are you white trash?")
ask_question("Do you think you can kickass?")
ask_question("Do you have a dark sense of humor?")
ask_question("Do you have a short temper?")
ask_question("Do you have a strong desire for money?")
ask_question("Are you often considered impulsive?")
ask_question("Are you self-centered?")
ask_question("Do you have a system for getting anything you want?")
ask_question("Do you think you are smart?")

if score >= 9:
    character = "Dennis"
elif score >= 6:
    character = "Frank"
elif score >= 3:
    character = "Mac"
elif score >= 0:
    character = "Dee" 
else:
    character = "Charlie"

print("Based on your answers you are most like ", character)


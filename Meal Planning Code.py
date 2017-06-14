import random
recipe_list = []
recipe_file = open("recipe_list.txt", "r")
for line in recipe_file:
    # print(line.strip())
    recipe_list.append(line.strip())

def random_gen():
    if len(choice_list) > 0:
        # remove user choices from recipe list
        recipe_list.remove(choice_list[-1])
    # generate random samples
    r1 = random.sample(recipe_list, 5)
    # print samples out with numbers to identify them
    for i in range(5):
        print(str(i+1) + ' ' + r1[i])
    return r1


# random_list = random_gen()
# user_choice = raw_input("\nChoose a Recipe Using Numbers 1-5, (Q) to Quit: ")
# ans = user_choice.lower()
choice_list = []
quit_list = ["q", "quit", "end", "finished", "finish", "exit"]
first_run = True

# add code to anticipate if a user uses a number not between 1-5
while first_run == True or ans not in quit_list:
    # generate new random list
    random_list = random_gen()
    # ask user to choose a recipe, save the response to a variable
    user_choice = raw_input("\nChoose a Recipe Using Numbers 1-5, (q) to Quit: ")
    try:
        # store user input as a list
        choice_list.append(random_list[int(user_choice)-1])
    except ValueError as e:
        pass
    ans = user_choice.lower()
    if ans != range(1, 6):
        print"Out of range, try again:"
    else:
        pass
    first_run = False

# print one new line before printing recipes
# print each recipe on a new line
print "\nYou Chose: "
for line in choice_list:
    print line




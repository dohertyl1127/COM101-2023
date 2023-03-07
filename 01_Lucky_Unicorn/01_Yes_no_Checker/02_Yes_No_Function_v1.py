def yes_no(question):
    while True:

        # ask user if they have played before
        response = input(question).lower()

        # if yes continue code
        if response == "yes" or response == "y":
            return "yes"
        # if no display instructions
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please choose yes/no")


# main routine goes here
show_instructions = yes_no("have you played before? ")
print("you choose {}".format(show_instructions))
print()
having_fun = yes_no("are you having fun? ")
print("you said {} to having fun ".format(having_fun))

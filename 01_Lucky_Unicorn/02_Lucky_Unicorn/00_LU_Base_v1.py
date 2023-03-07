# Functions go here

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


def instructions():
    print("****How To Play****")
    print()
    print("The rules of the game go here")
    print()
    return ""


# Main routine goes here
played_before = yes_no("have you played before? ")

if played_before == "no":
    instructions()

print("program continues")

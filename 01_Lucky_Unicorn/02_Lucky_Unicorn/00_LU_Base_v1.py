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
    print()
    print("****How To Play****")
    print()
    print("The rules of the game go here")
    print()
    return ""


def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # response if the amount is too high / low give
            if low < response <= high:
                return response

            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here
played_before = yes_no("have you played before? ")

if played_before == "no":
    instructions()

how_much = num_check("How much would you like to play with?", 0, 10)

print("you have asked to play with ${}".format(how_much))
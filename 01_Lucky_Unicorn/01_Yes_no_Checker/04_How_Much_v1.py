# Functions go here


# Main routine goes here

error = "Please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        # ask the question
        response = int(input("how much would you like to play with? "))

        # response if the amount is too high / low give
        if 0 < response <= 10:
            print("you have asked to play with ${}".format(response))

        # output an error
        else:
            print(error)

    except ValueError:
        print(error)

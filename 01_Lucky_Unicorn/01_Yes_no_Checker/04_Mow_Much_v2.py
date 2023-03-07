# Functions go here
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
while True:
    how_much = num_check("How much would you like to play with?", 0, 10)

    print("you have asked to play with ${}".format(how_much))

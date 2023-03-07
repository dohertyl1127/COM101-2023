
show_instructions = ""
while show_instructions.lower != "xxx":

    #ask user if they have played before
    show_instructions = input("have you played before? ")

    #if yes continue code
    if show_instructions.lower() == "yes" or "y":
        print("program continues")
    #if no display instrutions
    elif show_instructions.lower() == "no" or "n":
        print("display instructions")
    else:
         print("please choose yes/no")

print()
print("We are done!")

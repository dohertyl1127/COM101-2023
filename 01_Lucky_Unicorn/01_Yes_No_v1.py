#ask user if they have played before
show_instructions = input("have you played before? ")

#if yes continue code
if show_instructions.lower() == "yes":
    print("program continues")
elif show_instructions.lower() == "y":
    print("program continues")
#if no display instrutions
elif show_instructions.lower() == "no":
    print("display instructions")
elif show_instructions.lower() == "n":
    print("display instructions")
else:
     print("please choose yes/no")

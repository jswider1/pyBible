# control+c to stop program
known_users = ["Mary","Bob","Alice","Jane","Peewee","John","Denise"]

print("There are {} names on our security list.".format(len(known_users)))

while True:
    print("Hi! My name is security.")
    name = input("What is your name? ").strip().capitalize()

    if name in known_users:
        print("Welcome back {}!".format(name))
        remove = input("Would you like to be removed from the system? (y/n): ").lower()
        if remove == "y":
            known_users.remove(name)
            print("Sorry to see you go {}.".format(name))
        elif remove == "n":
            print("Excellent, I'm glad you're staying.")
            # del is a delete function too
            # del (known_users[2]) will remove the element in index 2
    else:
        print("You aren't registered with the system.")
        add_me = input("Would you like to be added to the list? (y/n): ").strip().lower()
        if add_me == "y":
            known_users.append(name)
            print("Excellent, welcome aboard, {}.".format(name))
        elif add_me == "n":
            print("Too bad, it would have been nice to have you, {}.".format(name))

# tuple our_tuple = 1,2,3,"A","B","C"  #inside parentheses or not    # also imutable
# type(our_tuple)           # tuples are safe ways to store data that u don't want changed
# tuple()  # function to convert other pieces of data to a tuple
# A = [1,2,3] tuple(A) will not change A, but will convert the output of A to be a tuple
# So, A = tuple(A) actually changes A to a tuple

# Multiple variables at once: (A,B,C) = 1,2,3  or D,E,F = [1,2,3]
# and G,H,I = "789", all create multiple variables at once


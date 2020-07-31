films = {
    "Shrek":[3,2],
    "Bourne":[17,2],
    "Kids":[17,2],
    "Dumbo":[3,2]
    }

while True:

    choice = input("What film would you like to watch? ").strip().title()

    if choice in films:
        # pass # tells the program to just pass this section by
        age = int(input("How old are you? ").strip())

        # check user age
        if age >= films[choice][0]:

            num_seats = films[choice][1]
            # check if enough seats remain
            if num_seats > 0:
                print("Enjoy the film. ")
                films[choice][1] = num_seats - 1
            else:
                print("Sorry, that film is sold out. ")
                
        else:
            print("You are too young, we can't allow you to see this film. ")
    else:
        print("We don't have that film currently.")
        

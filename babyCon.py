##number = 1
##
##while number <= 42:
##    if number % 2 != 0:
##        print(number)
##    number = number + 1

##L = []
##
##while len(L) < 3:
##    new_name = input("Please add a new name: ").strip().capitalize()
##    L.append(new_name)
##
##print("Sorry, list is full.")
##print(L)

##from random import choice
##
##questions = [
##    "What level do you want to get to? ",
##    "Why do we die? ",
##    "Why are people so stupid? ",
##    "Where are all the dinosaurs? "
##    ]
##question = choice(questions)
##
##answer = input(question).strip().lower()
##
##while answer != "just because":
##    answer = input("Why? ").strip().lower()
##
##print("Oh... Okay ")

##for letter in "abcd":
##    print(letter)
##
##for number in range(1,10,2):
##    print(number)

vowels = 0
consonants = 0

word = input("Give me a word, please. ").strip().lower()

for letter in word:
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1

print("There are {} vowels and {} consonants in {}.".format(vowels,consonants,word))


        

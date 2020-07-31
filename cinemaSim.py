# dictionaries:
students = {}
students = {"Alice":25,"bob":27,"Claire":17,"Dan":21,"Emma":22}
# items     keys    values
students["Dan"] # key
students["Fred"] = 25 # key of Fred and assign value
print("Alice is {}.".format(students["Alice"]))
students["Alice"] = 26
print("Now Alice is {}.".format(students["Alice"]))
# delete
del students["Fred"]
# give dictionary of keys
print(students.keys())
# turn dic into list
a = list(students.keys())
print("Now printing Dictionary of people as a LIST: {}".format(a))
print(a)
print("Dictionaries are iterable, but not indexable")

# dictionary 2 of students, with "keys"
students2 = {
    "male":["Bill","Frank","Tom","Chris"],
    "female":["Sarah","Jane","Kim","Emily","Crystal"]
    }

for key in students2.keys(): # create var "key"(and iterate) for the keys inside students2
    for name in students2[key]: # create var "name"(and iterate) for names inside each key of students2
        if "a" in name:
            print(name)

# List Comprehensions
even_numbers = [x for x in range(1,11) if x % 2 == 0]
print(even_numbers)
odd_numbers  = [x for x in range(1,11) if x % 2 != 0]
print(odd_numbers)
# creating list of words, then var "w" iterate through words to gather and manipulate data
words = ["the","quick","brown","fox","jumps","over","the","lazy","dog"]
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)

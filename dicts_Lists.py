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
print(students)
# Dictionaries will not store the keys in any particular order, which is why
# they are not indexable
# List ages for some keys
print(list(students.values())[2:])
# have to use a key to access dictionary

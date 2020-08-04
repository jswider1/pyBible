# functions and creating them
# simple add function example
#def add(x,y):
#    return = x + y

# reverse function
#def rev(text):
#    return text[::-1]

# Global Variable, make sure scopes do NOT overlap
a = 100

def f1():
    # Local Variable, which are destroyed when function is finished
    b = 90
    b = b + a
    print("Lacal variable 'b' being added to Global variable 'a' inside function 1 is [{}]".format(b))

def f2():
    # Local Variable
    a = 80
    print("Local variable 'a' from function 2 is [{}]".format(a))

f1()
f2()
print("Global variabe 'a' before function 3 is [{}]".format(a))
# global variable not changed from inside local functions
# unless the "global" function is used
def f3():
    d = 300
    global a
    a = a + d

f3()
print("Global variable 'a' after function 3 is [{}] ".format(a))

l = [1,2,3]
# however, can change a piece of global 'list' within a function
def f4():
    l[0] = 4

print("List l before function 4 is {} ".format(l))
f4()
print("List l after function 4 is now {} ".format(l))

# packing elements
print(1,2,3,4,5)
numbers = [1,2,3,4,5]
print("numbers is not unpacked here: {}".format(numbers))
# unpacking elements as iterating through
for number in numbers:
    print("numbers is now unpacked here: {}".format(number))
print("abc")
print(*"abc")
# one star * for normal arguments 'in order' / two star ** for 'key' arguments
def add(*numbers): # (*args)
    total = 0
    for number in numbers:
        total = total + number
    return(total)

print(add(1,2,3,4,5,6,7,8))

def about(name,age,likes):
    sentence = "Meet {}. They are level {} and they like {}.".format(name,age,likes)
    return sentence

print(about("Jack",42,"Python"))

dictionary = {"age":27, "likes":"IceCream","name":"Zack"}
# two star ** for 'key' arguments, where order doesn't matter
print(about(**dictionary))
print(about(likes="Cake",name="Pete",age=37)) # keys used so order doesn't matter

# another **kwargs example, dynamic number of arguments
def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key,value))

foo(widget1="purple",widget2="green")
foo(widget1="grey",widget2="silver",widget3="blue")
foo(widget4="brown",widget5="gold")
print(foo())
    



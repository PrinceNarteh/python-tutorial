# # string is any character within a quote - '', ""
# first_name = "Emmanuel"
# name = 'Emmanuel'
# print(first_name)
# print(name)

# # number - integer (int), floating point (float), complex number (complex)
# # integer - whole
# age = 15
# # floating point - numbers with decimals
# height = 5.4
# # complex number = 5i + 4

# # boolean - True / False

# # List 
# numbers = [1,1 ,2,2,3,3,3,5]

# # Dict
# person = {
#     "first_name": "John",
#     "last_name": "Doe",
#     "age":20
# }

# # set
# scores = {1,1,2,2,2,3,3,3,4,4,5,5}
# print(scores)

# # tuple
# cood = [str, int]
# coodX = ["x", 53]
# coodY = ["y", 54]


# STRINGS


from audioop import add
from email.policy import default
from multiprocessing import Condition


sentence = "The quick brown fox jumps over the lazy dog"
# print(sentence.count("o"))
# print(sentence.endswith("dog"))
# print(sentence.find("b"))
name = "              Prince Narteh"
age = 20
days = ["Monday", "Tuesday", "Wednesday"]
# new_sentence = "My name is {}. I am {} years old".format(name, "20")
# print(f"My name is {name}. I am {age} years old.")
# print(name.join("-"))
# print(name.strip())

# print(name.lower())


# NUMBERS
age = 20
# +, -, /, %, *, //

# print(2 + 2)
# print(2 - 2)
# print(2 / 2)
# print(2 * 2)
# print(12 % 3)
# print(10 // 3)


# numbers = [1,2,2,2,2,2,3,4,5,6,7,8,9,10]
# ages = [15,16,17,18,19]

# numbers.append(11)
# # numbers.clear()
# newAges = ages.copy()
# print(numbers)
# print(newAges)
# print(numbers.count(2))
# numbers.extend([12,13,14,15])
# print(numbers)
# numbers.insert(1, 19)
# print(numbers)
# print(numbers.index(4))
# numbers.pop()
# numbers.pop()
# numbers.pop(0)
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.remove(2)
# print(numbers)


# dictionary
# person = {
#     "first_name": "John",
#     "last_name": "Doe",
#     "age": 20,
#     "is_married": True,
#     "occupation": "Programmer"
# }

# person.update({"middle_name": "Jonny"})
# # person.setdefault({})
# person.pop("middle_name")
# # person.clear()
# # print(person.keys())
# # print(person.values())
# # print(person.items())
# # print(person.get("first_name"))
# # person.copy()
# # print(person)

# # Boolean 
# isMarried = False
# print(isMarried)

# # Set 
# scores = {1,1,2,2,2,3,3,4,4,4,5,5,5,5,6,6,6,7,8,8,8}
# # print(scores)



# CONTROL FLOW 
# if condition:
#     # code will run
# elif condition:
#     # second code runs
# else:
#     # default code runs

# age = int(input("Please enter your age: "))
# if age > 0 and age <= 18:
#     print("You can't vote")
# elif age > 18 and age < 40:
#     print("You can vote")
# elif age >= 40:
#     print("You can vote and also be President")
# else:
#     print("Please enter a valid age")


# FUNCTIONS
def greet(name):
    print(f"Welcome, {name}!")

# greet("Prince")
# greet("Emmanuel")

# def square(x):
#     total = x * x
#     return total

# nine = square(9)
# five = square(5)

# print(nine)
# print(five)

# CLASS 
class Student:
    def __init__(self, fname, lname, gender):
        self.first_name = fname
        self.last_name = lname
        self.gender = gender
    
    def desc(self):
        print(f"My name is {self.first_name} {self.last_name}. I am a {self.gender}")

prince = Student("Prince", "Narteh", "male")
print(prince.first_name)
print(prince.last_name)
print(prince.gender)
print(prince.desc())

"hello"
prince.
# First, create a variable



message = "Hello"

# Later, use it (even in a different cell)
print(message + " World!")

# Modify it
message = message.upper()
print(message)
age = 20
# Correct Python
if age > 18:
    print("Adult")

# Wrong - Python won't understand
#age > 18 print("Adult")

score =100

if score >90:
    print("A grade")
    if score == 100:
        print("Perfect!")



def greet(name):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello!")


def first_function():
    pass


def second_function():
    pass


long_string = (
    "This is a very long string that "
    "spans multiple lines for readability"
)
message = "Hello"
print(len(message))  # 5

empty = ""
print(len(empty))    # 0

age = 25
message = "I am " + str(age) + " years old"
print(message)  # I am 25 years old

# Or use f-strings (we'll learn more later)
message = f"I am {age} years old"

score = 85
if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    
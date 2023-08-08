# fungsi
def hello_world():
    print("Hello World")


hello_world()


# argument
# positional argument
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old")


greet("John", 25)


# default argument
def greet(name, age=30):
    print(f"Hello, {name}! You are {age} years old")


greet("Doe")


# keyword argument
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old")


greet(age=40, name="Yusuf")


# return statement
def add_numbers(a, b):
    jumlah = a + b
    return jumlah


result = add_numbers(5, 3)
print(result)


# output will none because it not use return
def greet(name):
    print(f"Hello, {name}!")


result2 = greet("xxx")
print(result2)

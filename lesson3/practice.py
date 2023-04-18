i = 1
while i < 10:
    print(i)
    i += 1

print(list(range(10)))

a = list(range(10, 20))
print(a)

b = list(range(10, 20, 2))
print(b)

for number in range(10):
    print(number)

a_dict = { "one": 1, "two": 2, "three": 3}
keys = a_dict.keys()
keys = sorted(keys)
for key in keys:
    print(key)


for number in range(10):
    if number % 2 == 0:
        print(number)

list = [1, 2, 3]

squares = [x ** 2 for x in range(10)]
print(squares)

squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)

odds = [x for x in range(10) if x % 2 != 0]
print(odds)

odds = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(10)]
print(odds)



a_dict = { "one": 1, "two": 2, "three": 3}
for key in a_dict:
    print(key)

for key, value in a_dict.items():
    print(f"key = {key}, value = {value}")

for value in a_dict.values():
    print(f"value = {value}")


first = []
for x in range(1, 5):
    for y in range(5, 1, -1):
        if x != y:
            first.append((x, y))

print(first)


second = [(x, y) for x in range(1, 5, 1) for y in range(5, 1, -1) if x != y]

print(second)

def hello_world():
    #Output hello world"""
    print("Hello World")


def square(n):
    s = n ** 2
    return s
    #print('Square area ' + str(s))



a = [1, 1.3, 28, 0.9]

for i in a:
    result = square(i)
    print(f'Square area with side {i} is equal {result}')



def foo(*args, **kwargs):
    print(args)
    print(kwargs)

abc = [1, 2, 3]
foo(*abc)   



'''


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


a_dict = {"one":1, "two":2, "three":3}
for key, value in a_dict.items():
    print(f"key = {key}, value = {value}",)

for value in a_dict.values():
    print(f"value = {value}")

for key in a_dict.keys():
    print(f"key = {key}")

for key in a_dict:
    print(f"key = {key}")

first = []

for x in range(1, 5):
    for y in range(5, 1, -1):
        if x != y:
            first.append((x, y))


print(first)
second = [(x, y) for x in range(1, 5) for y in range(5, 1, -1) if x != y]
print(second)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''

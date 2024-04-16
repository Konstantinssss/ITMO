def max_num(x, y):
    if x > y:
        print(x)
    elif x < y:
        print(y)
max_num(5, 2)

def num(x, y):
    if (x - y) > 135:
        print('YES')
    else:
        print('NO')
num(100, 150)

def month(x):
    if x == 12 or x == 1 or x == 2:
        print("зима")
    elif x in range(3, 6):
        print("весна")
    elif x in range(6, 9):
        print("лето")
    elif x in range(9, 12):
        print("осень")
month(6)

def num(x, y, z):
    if x+y+z > 10:
        print("YES")
    else:
        print("NO")
num(1, 2, 3)

def numbers(x):
    count = 0
    for y in x:
        if y >= 0:
            count = count + 1
    print(count)
numbers([1, 2, 3, -1, 5])

def count_days(x, y):
    x = x * (12 * 29)
    y = y * 29
    z = x + y
    print(z)
count_days(2, 5)
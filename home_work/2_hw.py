def task_1():

    int: int = 10
    float: float = 3.14
    str: str = "python"
    list: list = [1, 'one']
    bool: bool = True

    print("int:", type(int))
    print("float:", type(float))
    print("str:", type(str))
    print("list:", type(list))
    print("bool:", type(bool))

    return int, float, str, list, bool

task_1()

def task_2():
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[0:3]
print(task_2())

def task_3():
    a = int()
    return a ** 2
print(task_3())
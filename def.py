# def r(boy, girl):
#     print(f"{boy} loves {girl}")

# r("raghavendra", "ragini")


# def tables(num):
#     for i in range(1, 11):
#         print(f"{num} x {i} = {num * i}")


# tables (2)
# tables (3)
# tables (4) 

# def ragu(x):
#     return x * 2

# a = ragu(5)
# b = 10 + a 
# print(b)  # Output: 20


# def func():
#     a = input("enter your name: ")
#     print (f"hello {a}")
# func()


# def ragu():
#     a = int(input("enter the factorial number: "))
#     for i in range(1, a + 1):
#         if i == 1:
#             fact = 1
#         else:
#             fact = fact * i
#     print(f"factorial of {a} is {fact}")

# ragu()

# n = int (input ())
# if n%2 != 0:
#     print("Weird")
# elif n%2 == 0 and n == range(2,6):
#     print("Not Weird")
# elif n%2 == 0 and n == range(6,21):
#     print ("Weird")    
# elif n%2 == 0 and n == 10000000000000000000:
#     print("Not Weird")    


# n = int (input())
# m = []
# for ragu in range(0,n+1):
#     m[ragu] = ragu**2
#     print (m)

# n = int ( input ())
# for r in range(1,n+1):
#     print(str(r), end="")




# n = int(input())
# arr = map(int, input().split())
    
# sorted_arr = sorted(arr,reverse=True)
# for i in range(n+1):
#     if sorted_arr[i] != sorted_arr[i+1]:
#         print(sorted_arr[i+1])
#         break
#     else:
#         continue


def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b


while True:
    print("this is calculator")
    print ("enter 1 to do addition")
    print("enter 2 to do sub")
    print("enter 3 to do mul")
    c = int ( input())

    if (c == 1):
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        print(f"addition is {add(a,b)}")
        print()
        print()
        print("---------")
        print()
        print()
    elif (c == 2):
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        print(f"addition is {sub(a,b)}")
        print()
        print()
        print("---------")
        print()
        print()
    elif (c == 3):
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        print(f"addition is {mul(a,b)}")
        print()
        print()
        print("---------")
        print()
        print()

    else :
        print("invalid input")
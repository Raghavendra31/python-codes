# class ragu:
#     def __init__(self, num):
#         self.num = num

#     def tables(self):
#         for i in range(1, 11):
#             print(f"{self.num} x {i} = {self.num * i}")

#     def ragu(self, x):
#         return x * 2

#     def greet(self):
#         a = input("enter your name: ")
#         print(f"hello {a}")

#     def factorial(self):
#         a = int(input("enter the factorial number: "))
#         fact = 1
#         for i in range(1, a + 1):
#             fact *= i
#         print(f"factorial of {a} is {fact}")


# a = ragu(111)
# a.tables()




class ragu:
    def __init__(self,name):
        self.name = name
    def dog(self):
        print(f"hello{self.name}")


a = ragu("ragu")
print (a)
a.dog()


print (a)
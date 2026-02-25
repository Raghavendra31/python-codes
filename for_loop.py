# i = "raghavendra"

# for letter in i:
#     print (letter)


# # enumarate example

# l = [1,2,3,4,5]
# for index, value in enumerate(l):
#     print (f"index: {index}, value: {value}")


# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} X {j} = {i * j}")


# a= [1 , 23,54 ,55 , 67, 78, 89, 90, 100]
# total = 0
# for i in a:
#     total += i
# print(f"Total sum of the list is: {total}")


a = {"Name": "Raghavendra",
     "Age": 30,
     "City": "Bangalore",
     "Occupation": "Software Engineer"}

for key, value in a.items():
    print(f"{key}: {value}")

# a = ["raghavendra", "kumar", "reddy"]
# marks = [90, 80, 70]
# total = {}
# for index, name in enumerate(a):
#     total[name]= marks [index]
# print(total)


# comphrehension examples


# l = [1, 2, 3, 4, 5]
# dl = [item**2 for item in l]  # dl = { equation for item in collection }
# print(dl)

# for i in range(1,11):
#     dl = i**2 
#     print(dl,end=" ")


# new comprehension example

# l = [1, 2, 3, 4, 5]
# dl = [item**2 for item in l if item % 2 != 0]  # Only squares of even numbers
# print(dl)

# a = ["raghavendra", "kumar", "reddy"]

# cl =[item[1] for item in a ]
# print (cl)


# a = ["raghavendra", "kumar", "reddy"]

# da = {item : len(item) for item in a}
# print(da)
# dda = {}
# for index, item in enumerate(a):
#     dda[item] = len(item)
# print(dda)

# a= input("Enter a list of numbers separated by spaces: ").split()

# print (a)

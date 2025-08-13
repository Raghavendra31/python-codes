# # while loop example

# is_failed = True 
# i = 1
# while is_failed :
#     print(f"attempt {i}")
#     i += 1


# is_failed = True
# i =0 
# while is_failed:
#     if i%2 != 0:
#         print(f"attempt {i}")
#         i += 1
#         continue
#     i += 1
#     if i > 10:
#         is_failed = False


#atm code

pin = "1234"
attempts = 1
while attempts <=3:
    enter_pin = input("enter the pin ")
    if enter_pin==pin:
        print ("pin is correct")
        break
    else:
        print ("incorrect pin")
        attempts += 1
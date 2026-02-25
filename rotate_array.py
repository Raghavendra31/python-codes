# def rotate_left(arr,k):
#     n = len(arr)
#     k %= n
#     return arr[k:] + arr[:k]


# def rotate_right(arr,k):
#     n = len(arr)
#     k %= n
#     return arr[-k:] + arr[:-k]



# arr = [1,2,3,4,5,6]
# print( rotate_left(arr,8))
# print( rotate_right(arr,8))



def rotate(arr, side, k ):
    n = len(arr)
    k %= n
    if (side == "left"):
        return arr[k:] + arr[:k]
    else:
        return arr[-k:] + arr[:-k]
    

arr = [1,2,3,4,5,6]
print(rotate(arr, "left", 2))
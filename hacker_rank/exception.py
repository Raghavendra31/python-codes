while True:
    try:
        i = int(input("enter the number : "))
        r = 1/i
        print(r)
        break

    except Exception as e:
        print(f"enter the value correctly, your are {e}")

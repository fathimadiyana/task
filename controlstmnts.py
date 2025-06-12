while True:
    num = int(input("Enter a number : "))

    if num == 0:
        print("Stop the progrm.")
        break

    if num < 0:
        print("Neg number")
        continue

    if num % 2 == 0:
        print("Even number.")
    elif num % 3 == 0:
        print("Divisible by 3.")
    else:
        print("Odd number  not divisible by 3.")

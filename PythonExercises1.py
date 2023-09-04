# We take a celsius float input from the user and convert to Fahrenheit with two decimal places
def find_size(x):
    i = 0

    while True:
        i += 1
        x = x // 10

        if x == 0:
            break

    return i


def temp_converter():
    print("Enter the celsius temperature:", end=" ")
    celsius = float(input())
    fahrenheit = float((9/5 * celsius)+ 32)
    print("Fahrenheit:", end=" ")
    print(f"{round(fahrenheit, 2):.2f}")
    menu()


def find_max():
    print("Enter three integers:", end=" ")
    inp = int(input())
    maxi = inp % 10
    inp = inp // 10
    i = 0
    while i != 2:
        maxi2 = inp % 10
        if maxi < maxi2:
            maxi = maxi2
        inp = inp//10
        i += 1
    print("Max:", end=" ")
    print(maxi)
    menu()


def disp_high_low_number():
    print("Please enter a number:", end=" ")
    inp = int(input())
    k = find_size(inp)
    numbers = [0] * k
    n = k-1
    maxi = 0
    while n > -1:
        numbers[n] = inp % 10
        inp = inp // 10
        n -= 1

    i = 0
    while i < k:
        if numbers[i] > maxi:
            maxi = numbers[i]
        i += 1

    l = 0
    mini = maxi
    while l < k:
        if numbers[l] < mini:
            mini = numbers[l]
        l += 1

    print("Number of digits in the given number is: " + str(k))
    print("Smallest number is: " + str(mini))
    print("Highest number is: " + str(maxi))
    menu()


def sum_all():
    print("Please enter a number:", end=" ")
    inp = int(input())
    i = 1
    total = 0
    while i <= inp:
        total = total + i
        i += 1
    print("Total is " + str(total))
    menu()


def menu():
    print("Please select the feature you would like to try?")
    print("1. Celsius to Fahrenheit")
    print("2. Find the maximum")
    print("3. Display the highest, lowest and number of integers")
    print("4. Sum of all numbers from 1 to N printer")
    print("5. Exit")
    print("Enter here:", end=" ")
    choice = int(input())

    if choice == 1:
        temp_converter()
    elif choice == 2:
        find_max()
    elif choice == 3:
        disp_high_low_number()
    elif choice == 4:
        sum_all()
    elif choice == 5:
        quit()
    else:
        print("Try again")
        menu()


menu()






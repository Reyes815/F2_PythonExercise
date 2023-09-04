from array import *

def int_to_strlist(bin):
    strlist = str(bin)
    x = [i for i in strlist]
    return(x)

def list_inverter(list1):
    k = len(list1)
    list2 = [0] * k
    i = 0
    j = k
    while i < k:
        list2[i] = list1[j-1]
        i += 1
        j -= 1
    return list2


def decToBinary(dec):
    list1=[]
    index = 0
    while(dec > 0):
        x = dec
        if x % 2 == 0:
            list1.append(0)
        if x % 2 == 1:
            list1.append(1)
        dec = dec // 2
        index += 1
    final = list_inverter(list1)
    print(final)
    main()


def binaryToN(bin, type):
    binlist = list(map(int, str(bin)))
    binlist = list_inverter(binlist)
    size = len(binlist)
    if type == 1:
        i = 0
        dec = 0
        while (i < size):
            if binlist[i] == 1:
                dec = dec + 2**i
            else:
                continue
            i += 1
        return dec
    elif type == 2:
        table = {000: '0', 001: '1', 010: '2', 011: '3', 100: '4',
             101: '5', 110: '6', 111: '7'}


        return
    elif type == 3:
        return
    else:
        print("Try again")
    main()


def decToOctal(dec):
    list1=[]
    index = 0
    while(dec > 0):
        x = dec
        remainder = x % 8
        list1.append(remainder)
        dec = dec // 8
        index += 1
    final = list_inverter(list1)
    print(final)
    main()


def decToHex(dec):
    table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
             5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
             10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex = ''
    while(dec > 0):
        rem = dec % 16
        hex = table[rem] + hex
        dec = dec // 16
    print(hex)
    main()



def main():
    print("Please select the feature you would like to try?")
    print("1. Decimal to Binary")
    print("2. Binary to type of your choice")
    print("3. Decimal to Octal")
    print("4. Decimal to Hexadecimal")
    print("5. Exit")
    print("Enter here:", end=" ")
    choice = int(input())

    if choice == 1:
        print("Give me a decimal number: ", end="")
        inp = int(input())
        decToBinary(inp)
    elif choice == 2:
        print("Give me a binary number: ", end="")
        inp = int(input())
        print("1. Decimal")
        print("2. Octal")
        print("3. hexadecimal")
        print("Select what type: ", end="")
        type = int(input())
        binaryToN(inp, type)
    elif choice == 3:
        print("Give me a decimal number: ", end="")
        inp = int(input())
        decToOctal(inp)
    elif choice == 4:
        print("Give me a decimal number: ", end="")
        inp = int(input())
        decToHex(inp)
    elif choice == 5:
        quit()
    else:
        print("Try again")
        main()


main()


# Function to find two missing

def findTwoMissingNumbers(arr, n):
    XOR = arr[0]
    for i in range(1, n - 2):
        XOR ^= arr[i]
    for i in range(1, n + 1):
        XOR ^= i
    set_bit_no = XOR & ~(XOR - 1)
    x = 0
    y = 0
    for i in range(0, n - 2):
        if arr[i] & set_bit_no:
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    for i in range(1, n + 1):
        if i & set_bit_no:
            x = x ^ i
        else:
            y = y ^ i
    print("Two Missing Numbers are\n%d %d" % (x, y))
arr = [1, 3, 3, 4, 5]
n = 2 + len(arr)
findTwoMissingNumbers(arr, n)


def getTwoElements(arr, n):
    global x, y
    x = 0
    y = 0

    xor1 = arr[0]

    for i in range(1, n):
        xor1 = xor1 ^ arr[i]

    for i in range(1, n + 1):
        xor1 = xor1 ^ i

    set_bit_no = xor1 & ~(xor1 - 1)

    for i in range(n):
        if (arr[i] & set_bit_no) != 0:

            # arr[i] belongs to first set
            x = x ^ arr[i]
        else:

            # arr[i] belongs to second set
            y = y ^ arr[i]

    for i in range(1, n + 1):
        if (i & set_bit_no) != 0:

            # i belongs to first set
            x = x ^ i
        else:

            # i belongs to second set
            y = y ^ i

    # x and y hold the desired
    # output elements


# Driver code
arr = [1, 3, 4, 5, 5, 6, 2]
n = len(arr)

getTwoElements(arr, n)

print("The missing element is", x,
      "and the repeating number is", y)
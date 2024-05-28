arr = [1, 2, 4, 3, 6]  # so the length of this array is always equal to n - 1 numbers
n = 6  # so there is supposed to be five numbers


# summation approach
def find_number(arr, n):
    # sum of natural numbers from 1 to n
    sum_n = int(n * ((n + 1) / 2))
    sum_r = 0
    for val in arr:
        sum_r += val
    return sum_n - sum_r


# result = find_number(arr, n)


def find_number_xor(arr, n):
    xor1, xor2 = 0, 0
    for i in range(n - 1):
        xor1 ^= arr[i]
        xor2 ^= i + 1  # with i + 1 to escape 0 index
    xor2 ^= n  # to cancel pairs formed
    return xor2 ^ xor1


result = find_number_xor(arr, n)
print(result)


# print(result)

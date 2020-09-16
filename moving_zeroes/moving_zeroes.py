'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    non_zeros = []
    zeros = []

    for i in arr:
        if i == 0:
            zeros.append(i)
        else:
            non_zeros.append(i)

    return non_zeros + zeros


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
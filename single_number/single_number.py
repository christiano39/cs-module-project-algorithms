'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# def single_number(arr):
#     counts = {}
#     for i in arr:
#         if i in counts:
#             counts[i] += 1
#         else:
#             counts[i] = 1

#     for num in counts:
#         if counts[num] == 1:
#             return num

def single_number(arr):
    s = set()

    for num in arr:
        if num in s:
            s.remove(num)
        else:
            s.add(num)

    return list(s)[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
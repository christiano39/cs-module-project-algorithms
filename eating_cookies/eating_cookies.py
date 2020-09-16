'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    from sys import argv
    num_cookies = int(argv[1])

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

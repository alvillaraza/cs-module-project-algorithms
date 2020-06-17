'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    #loop through and check if element == 0
    for i in arr:
        zero = []
        if arr[i] == 0:
            zero.append(arr[i])

            print(zero)
            
    #if it's 0, move index +1

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
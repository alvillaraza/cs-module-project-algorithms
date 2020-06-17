'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    _size = len(arr)
#create a array of zeros
    zero = []
# create an array of numbers
    numbers = []
    for i in range(_size):
        #**If number in the index equals 0...
        if arr[i] == 0:
            cur_index = arr[i]
            # print('current element', arr[i])
            #**put that number in the zero array
            zero.append(cur_index)
            # print('zero array = ', zero, 'end---')

        #**If number in the index does not equal 0...
        if arr[i] != 0:
            cur_index = arr[i]
            #**put that number in the numbers array
            numbers.append(cur_index)
            # print('numbers array=', numbers, 'end===')
    # print(numbers + zero)
#**combine the arrays together
    return numbers + zero


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
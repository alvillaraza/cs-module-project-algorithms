'''
Input: a List of integers
Returns: a List of integers
'''
def multiplyList(arr):
    result = 1
    for x in arr:
        result = result * x
    return result

def product_of_all_other_numbers(arr):
    # Your code here
    _size = len(arr)
    #create a new array...multiplied = []
    multiplied = []
    for i in range(_size):
        cur_index = []
        # cur_index = i
        # print(arr[i])
    #pop out(remove) the current index
        number_taken_out = arr.pop(i)
        cur_index.append(number_taken_out)
        # print('number removed', cur_index)
        # print('array with removed number', arr)
        # print('index', i)
    #multiply the numbers in the array
        multiplied_number = multiplyList(arr)
        # print(multiplied_number)
    
    #append the new number into the multiplied = []
        multiplied.append(multiplied_number)
        # print('multiplied array = ', multiplied)

    #put the cur_index back into the array    
        arr.insert(i, *cur_index)
        # print(arr, 'end---')
    return multiplied


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

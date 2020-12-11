'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # create a frequency variable as a dictionary
    # count frequency of numbers
    # search through frequency to find the frequency of 1
    #return number that has a freq of one
    frequency = {}
    for num in arr:
        #if num is not in frequency yet, then add it with as num
        if num not in frequency:
            frequency[num] = 1
        #if num is already in frequency, increment count by 1
        else:
            frequency[num] += 1
    # print("frequency", frequency)
    for num, count in frequency.items():
        if count == 1:
            return num



    # alt
    #sort array in place
    #look check if first 2 match, then check next two until they don't match
    # if they don't match, return the first number.
    # if it's the last item, the loop will complete before it covers the last item, so we return the last item




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
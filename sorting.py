"""File containing implementations of various sorting algorithms"""

from random import randint

# Beginning of mergesort functions
def mergesort_merge(arr, start_index, end_index):
    """
    Starting from the left-most index and ending at the right-most index, merge
    both halves of this section of the list in a sorted manner.
    Input: arr is a list of comparable values
           start_index is the start index of the left half
           end_index is the last index of the right half
    Output: None, modifies original list
    """
    # We have left half starting position and right half ending position, so we
    # calculate the ending position of the left half and starting position of
    # the right half
    left_end = (end_index+start_index)//2
    right_start = left_end+1

    # Counters we'll use to keep track of our position in our while loop!
    left_index = start_index
    right_index = right_start

    # Temporary array to merge the left and right halves into.
    temp_arr = []

    # While we are still within range of our left and right halves, we sort!
    while(left_index <= left_end and right_index <= end_index):
        if arr[left_index] <= arr[right_index]:
            temp_arr.append(arr[left_index])
            left_index+=1
        
        else:
            temp_arr.append(arr[right_index])
            right_index+=1

    # Whichever half we did not fully explore, we extend it to the temporary 
    # array, since it still has values in it.
    if left_index > left_end:
        temp_arr.extend(arr[right_index:end_index+1])
    else:
        temp_arr.extend(arr[left_index:left_end+1])
    
    # Now we modify our original list!!
    arr[start_index:end_index+1] = temp_arr


def mergesort_helper(arr, start_index, end_index):
    """
    Recursive function that continuously divides the array in halves to be 
    later merged in a sorted order.
    """
    
    # Base Case, we've gotten down to one element. This base case also handles 
    # the empty list because of how the wrapper function initially calls this
    # function.
    if start_index >= end_index:
        return

    middle = (start_index+end_index)//2

    # Cut the left and right halves until we are only looking at one item
    mergesort_helper(arr, start_index, middle)
    mergesort_helper(arr, middle+1, end_index)

    # The sorting and merging happens here.
    mergesort_merge(arr, start_index, end_index)

def mergesort(arr):
    """
    Wrapper function that calls our helper function with initial arguments for 
    the entire array to be sorted.
    Input: List of comparable elements
    Output: None
    """
    mergesort_helper(arr, 0, len(arr)-1)

# Beginning of heapsort functions
def build_max_heap(arr):
    for i in range((len(arr)-2)//2, -1, -1):
        heapify(arr, len(arr), i)

def heapify(arr, end, parent_index):
    left_childi = parent_index*2+1
    right_childi = parent_index*2+2
    max_index = parent_index

    if left_childi < end and arr[left_childi] > arr[parent_index]:
        max_index = left_childi

    if right_childi < end and arr[right_childi] > arr[max_index]:
        max_index = right_childi

    if max_index != parent_index:
        arr[parent_index], arr[max_index] = arr[max_index], arr[parent_index]
        heapify(arr, end, max_index)

def heapsort(arr):
    """
    Our wrapper function that first calls to build a max heap and then loops to 
    adjust the max heap every time the max element of the heap is sorted out.
    Input: List of comparable elements
    Ouput: None, modifies input list
    """
    build_max_heap(arr)

    # Loop from end of list to start so that 
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Beginning of quicksort functions

def partition(arr, left_index, right_index, pivot):
    # print("pivot is {}".format(pivot))
    while(left_index <= right_index):
        while(arr[left_index] < pivot):
            # print('left_index is {} with pivot {}'.format(arr[left_index], pivot))
            left_index += 1
        
        while(arr[right_index] > pivot):
            # print('right_index is {} with pivot {}'.format(arr[right_index], pivot))
            right_index -= 1

        if (left_index <= right_index):
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
            left_index += 1
            right_index -= 1
        # print('arr after switch is {}'.format(arr))
    return left_index

def quicksort_helper(arr, start_index, end_index):
    if start_index >= end_index:
        return
    pivot = arr[randint(start_index, end_index)]
    # pivot = arr[(start_index+end_index)//2]
    index = partition(arr, start_index, end_index, pivot)
    quicksort_helper(arr, start_index, index-1)
    quicksort_helper(arr, index, end_index)

def quicksort(arr):
    quicksort_helper(arr, 0, len(arr)-1)


def main():
    a = [9, 12, 6, 13, 25, 4, 15, 7, 1, 3, 19]
    print(a)
    quicksort(a)
    print(a)
    b = [9, 12, 6, 13, 25, 4, 15, 7, 1, 3, 19]
    print(b)
    mergesort(b)
    print(b)
    c = []
    mergesort(c)
    print(c)

if __name__ == "__main__":
    main()
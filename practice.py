from random import *

def quicksort(num_list):
    """Quick Sort function to recursively sort a list of numbers. 
    Handles duplicates!"""
    if len(num_list) <= 1:
        return num_list

    else:
        index = randint(0, len(num_list)-1)
        randnum = num_list[index]
        less_list = []
        more_list = []
        for i in range(len(num_list)):
            if i == index:
                pass
            elif num_list[i] < randnum:
                less_list.append(num_list[i])
            else:
                more_list.append(num_list[i])
        
        return quicksort(less_list) + [randnum] + quicksort(more_list)

def main():
    ls = [4, 7, 0, 6, 9, 1, 5, 3, 8, 2]
    print('ls is {}'.format(ls))
    print('the sorted ls list is {}'.format(quicksort(ls)))

if __name__ == "__main__":
    main()
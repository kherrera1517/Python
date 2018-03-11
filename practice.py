from random import randint

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

def reverse32int(num):
    neg_num = False
    if num < 0:
        neg_num = True
        num *= -1
    
    rev_num = 0

    while (num != 0):
        rev_num = rev_num*10 + num%10
        num //= 10

    if neg_num:
        rev_num *= -1

    largest32num = 2**31-1
    smallest32num = ~largest32num

    if rev_num > largest32num:
        return 0

    elif rev_num < smallest32num:
        return 0
    
    else:
        return rev_num

def isnum_palindrome(num):
    if num < 0:
        return False

    elif num < 10:
        return True

    divisor = 1

    while(num//divisor >= 10):
        divisor *= 10

    while(num != 0):
        left = num//divisor
        right = num%10

        if left != right:
            return False
        
        num = (num%divisor)//10

        divisor //= 100

    return True

def isrec_numpalindrome(num):
    if num < 0:
        return False

    if num < 10:
        return True

    return rec_numpalindrome(num)

def rec_numpalindrome(num):
    if num < 10:
        return True
    divisor = 1
    while(num//divisor >= 10):
        divisor *= 10

    left = num//divisor
    right = num%10
    new_num = (num%divisor)//10


    if rec_numpalindrome(new_num):
        if left != right:
            return False
        else:
            return True

    else:
        return False

def roman_to_int_nonoptimal(roman):
    number = 0
    index = 0
    
    while(index < len(roman)):
        print('index is {}'.format(index))
        print('current char is {}'.format(roman[index]))
        print('current number is {}'.format(number))
        if roman[index] == 'I':
            if (index+1) < len(roman):
                if roman[index+1] == 'V':
                    number += 3
                    index += 1
                
                elif roman[index+1] == 'X':
                    number += 8
                    index += 1

           
            number += 1
            index += 1

        elif roman[index] == 'V':
            number += 5
            index += 1

        elif roman[index] == 'X':
            if (index+1) < len(roman):
                if roman[index+1] == 'L':
                    number += 30
                    index += 1
                
                elif roman[index+1] == 'C':
                    number += 80
                    index += 1


            print("saw X")
            number += 10
            index += 1
        
        elif roman[index] == 'L':
            number += 50
            index += 1
            print("saw L")

        elif roman[index] == 'C':
            if (index+1) < len(roman):
                if roman[index+1] == 'D':
                    number += 300
                    index += 1

                elif roman[index+1] == 'M':
                    number += 800
                    index += 1

            number += 100
            index += 1
            print("saw C")

        elif roman[index] == 'D':
            number += 500
            index += 1
            print("saw D")

        elif roman[index] == 'M':
            number += 1000
            index += 1
            print("saw M")
        
        else:
            print('did not match any cases')

        # elif roman[index] == 'X':S
        #     if (index+1) < len(roman) and roman[index+1] == 'I':
            
        print('current number after running while loop is {}'.format(number))

    return number

def roman_to_int(roman):

    num_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0

    for index in range(len(roman)):
        if index > 0 and num_dict[roman[index]] > num_dict[roman[index-1]]:
            number += num_dict[roman[index]] - 2*num_dict[roman[index-1]]
        else:
            number += num_dict[roman[index]]

    return number

def longest_common_prefix(strlist):
    if len(strlist) < 1:
        return ""

    elif len(strlist) < 2:
        return strlist[0]

    else:
        longest_common = lcp_helper(strlist[0], strlist[1])

        for i in range(2,len(strlist)):
            longest_common = lcp_helper(longest_common, strlist[i])

        return longest_common

def lcp_helper(str1, str2):

    if str1 == "" or str2 == "":
        return ""

    return_string = ""

    if len(str1) < len(str2):
        smallest_str =  str1
        largest_str = str2
    else:
        smallest_str = str2
        largest_str = str1

    for index in range(len(smallest_str)):
        if smallest_str[index] == largest_str[index]:
            return_string += smallest_str[index]
        
        else:
            break
    
    return return_string

def valid_parentheses(string):
    paren_map = {'(': ')', '{': '}', '[': ']'}
    closing = ']})'
    close_str = ""

    if string[0] in closing:
        return False

    for char in string:
        if char in paren_map:
            close_str = paren_map[char] + close_str

        elif char in closing:
            if close_str == "":
                return False

            elif char == close_str[0]:
                close_str = close_str[1:]

            else:
                return False

    if close_str == "":
        return True

    else: 
        return False

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return_str = str(self.val)
        curr = self.next
        while curr is not None:
            return_str += "->" + str(curr.val)
            curr = curr.next
        return return_str

def mergeTwoLists(l1, l2):
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    else:
        if l1.val<l2.val:
            new_node = ListNode(l1.val)
            new_node.next = mergeTwoLists(l1.next, l2)
            return new_node
        else:
            new_node = ListNode(l2.val)
            new_node.next = mergeTwoLists(l1, l2.next)
            return new_node

# def remove_duplicates_while(nums):
#     length = len(nums)
#     index = 0

#     while(index<length-1):
#         # print(index)
#         # print(length)
#         if nums[index] == nums[index+1]:
#             nums.remove(nums[index])
#             length-=1
#         else:
#             index +=1
#     return len(nums)

def remove_duplicates(nums):
    """"""
    if len(nums) == 0:
        return 0
    
    i = 0
    for j in range(len(nums)-1):
        if(nums[j+1] != nums[i]):
            i+=1
            nums[i] = nums[j+1]

    return i + 1

# def remove_element(arr, element):
#     arr_len = len(arr)
#     if arr_len == 0:
#         return 0

#     i = 0
#     j = arr_len - 1
#     while(i != j):
#         # print("i and j are {} and {}".format(i,j))
#         if arr[j] == element:
#             j -= 1
#             continue
#         if arr[i] == element:
#             arr[i], arr[j] = arr[j], arr[i]
#             i += 1
#         else:
#             i += 1

#     return i

def remove_element_1sttry(arr, element):
    arr_len = len(arr)
    if arr_len == 0:
        return 0

    i = 0
    j = arr_len - 1
    while(i < j):
        # print("i and j are {} and {}".format(i,j))
        if arr[i] != element:
            # print('should come in here for arr i')
            i += 1
        elif arr[j] == element:
            # print('should come in here for arr j')
            j -= 1
        else:
            # print('should come in here')
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    return arr[:i]

def remove_element(arr, element):
    length = len(arr)
    if length == 0:
        return length

    elif length == 1:
        if arr[0] == element:
            return 0
        else:
            return length
    else:
        i = 0
        for j in range(len(arr)):
            if(arr[j] != element):
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        return i
            

# Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap
# NOT MY OWN
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)
 
# Driver code to test above
# arr = [ 12, 11, 13, 5, 6, 7]
# heapSort(arr)
# n = len(arr)
# print ("Sorted array is")
# for i in range(n):
#     print ("%d" %arr[i])

# def merge(arr, left, middle, right):
#     print('hi')

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[l + i]
 
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr,l,r):
    if l < r:
 
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l+r)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

# def mergeSort(arr, left, right):
#     if left < right:
#         mid = length_arr//2

#         mergeSort(arr, left, mid)
#         mergeSort(arr, mid+1, right)
#         merge(arr, l, m, r)

def needle_in_haystack(haystack, needle):
    need_len = len(needle)
    hay_len = len(haystack)
    if needle == "":
        return 0
    else:
        for j in range(hay_len):
            if need_len > hay_len:
                break
            elif haystack[j] == needle[0]:
                if haystack[j:(j+need_len)] == needle:
                    return j

    return -1

def search_insert_position(nums, val):
    """No Duplicates in original nums list"""
    if nums == []:
        return 0
    for i in range(len(nums)):
        if nums[i] >= val:
            return i
        # elif nums[i] < val and nums[i+1] > val:
        #     return i + 1
    return i+1

def countandsayhelper(num_string):
    # print('num_string is {}'.format(num_string))
    len_str = len(num_string)
    return_string = ""
    if len_str < 1:
        # print('only here gives empty')
        return return_string
    elif len_str == 1:
        return '1' + num_string
    else:
        i = 1
        for j in range(len_str-1):
            if num_string[j] == num_string[j+1]:
                i += 1
            else:
                return_string += str(i) + num_string[j]
                i = 1
        if num_string[-1] != num_string[-2]:
            return_string += "1" + num_string[-1]
        else:
            return_string += str(i) + num_string[j]
        # print("doesn't modify this")
        return return_string


def countandsay(n):
    return_string = "1"
    while(n>1):
        return_string = countandsayhelper(return_string)
        n -= 1
    return return_string

def max_subarray(nums):
    nums_len = len(nums)
    temp_sum = 0
    max_sofar = float("-inf")
    for i in range(nums_len):
        temp_sum += nums[i]
        if temp_sum > max_sofar:
            max_sofar = temp_sum
        if temp_sum < 0:
            temp_sum = 0
    return max_sofar

def subarray_degree(nums):
    left, right, count = {}, {}, {}
    for index, num in enumerate(nums):
        if num not in left:
            left[num] = index
        right[num] = index
        count[num] = count.get(num, 0) + 1
    answer = len(nums)
    degree = max(count.values())

    for num in count:
        if count[num] == degree:
            answer = min(answer, right[num]-left[num]+1)

    return answer

def length_of_lastword(string):
    if string == "":
        return 0
    else:
        return_len = 0
        first_seen = False
        for i in range(len(string)-1,-1,-1):
            if string[i] != ' ':
                return_len += 1
                first_seen = True
            elif first_seen:
                break
        return return_len

def add_binary(str1, str2):
    if str1 == "":
        return str2
    elif str2 == "":
        return str1
    if str1[-1] == '0' and str2[-1] == '0':
        return add_binary(str1[:-1], str2[:-1]) + '0'
    elif (str1[-1] == '1' and str2[-1] == '0') or (str1[-1] == '0' and str2[-1] == '1'):
        return add_binary(str1[:-1], str2[:-1]) + '1'
    else:
        return add_binary(add_binary(str1[:-1],str2[:-1]),'1') + '0'

def plus_one(digits):
    if len(digits) < 1:
        return digits
    elif len(digits) == 1 and digits[0] == 9:
        return [1, 0]
    else:
        if digits[-1] == 9:
            newlist = plus_one(digits[:-1])
            newlist.append(0)
            return newlist
        else:
            digits[-1] = digits[-1] + 1
            return digits

def delete_duplicates_linkedlist(head):
    if head is None:
        return None
    curr_node = head
    curr_val = curr_node.val
    while(curr_node.next is not None):
        if curr_val == (curr_node.next).val:
            curr_node.next = (curr_node.next).next
        else:
            curr_node = curr_node.next
            curr_val = curr_node.val
            
    return head

def remove_element_linkedlist(head, val):
    if head is None:
        return None
    curr_node = head
    while(curr_node.next is not None):
        if (curr_node.next).val == val:
            curr_node.next = (curr_node.next).next
        else:
            curr_node = curr_node.next

    if head.val == val:
        head = head.next
    return head

def delete_node(node):
    if node.next is not None:
        node.val = (node.next).val
        node.next = (node.next).next
    else:
        node = None

def get_intersect_linkedlist(headA, headB):
    if headA is None or headB is None:
        return None
    match = False
    currA = headA
    currB = headB
    intersect_node = None
    while(True):
        if currA.val == currB.val:
            if not match:
                match = True
                intersect_node = currA
        else:
            match = False
            intersect_node = None

        if currA.next is None:
            if currB.next is None:
                break
            else:
                currA = headB
        else:
            currA = currA.next
        
        if currB.next is None:
            currB = headA
        else:
            currB = currB.next

    return intersect_node

def common_restaurants(list1, list2):
    shortest = float('inf')
    common = {}
    for index1, string1 in enumerate(list1):
        for index2, string2 in enumerate(list2):
            if string1 == string2:
                index = index1+index2
                common[string1] = index
                if index < shortest:
                    shortest = index
    
    returnlist = []
    for item in common:
        if common[item] == shortest:
            returnlist.append(item)

    return returnlist

# def prefix_to_infix(prefixes):
#     if len(prefixes) < 1:
#         return []
#     return_arr = []
#     digits = ['1','2','3','4','5','6','7','8','9']
#     for i in range(len(prefixes)):
#         temp = ""
#         left = ""
#         right = ""
#         for j in range(len(prefixes[i])-1,-1,-1):
#             if prefixes[i][j] in digits:
#                 if right:
#                     left = prefixes[i][j]
#                 else:
#                     right = prefixes[i][j]
#             else:
#                 temp = left + prefixes[i][j] + right
#                 temp = right

def prefix_to_suffix(prefixes):

    return_arr = []
    for i in range(len(prefixes)):
        return_arr.append(pref2suff(prefixes[i]))

    return return_arr

def pref2suff(pref):
    # digits = ['1','2','3','4','5','6','7','8','9']
    op_precedence = {'/':1, '*':2,'+':3, '-':4}
    operands = ['/', '*', '+','-']
    left = ""
    right = ""
    operators = []
    if len(pref) < 3:
        return pref
    else:
        if pref[0] in operands:
            if pref[1] in operands:
                i = 1
                while(pref[i] in operands):
                    i+=1
                temp_nums = ""
                j = i
                k = i
                while(j>0):
                    temp_nums += pref[i]
                    j -= 1
                    i += 1




                if op_precedence[pref[0]] < op_precedence[pref[1]]:
                    left = pref[2:4] + pref[0]
                    right = pref[1]
                    return left + pref2suff(pref[4:]) + right
                else:
                    left = pref[2:4] + pref[1]
                    right = pref[0]
                    return left + pref2suff(pref[4:]) + right
            else:
                left = pref[1]
                right = pref[0]
                return left + pref2suff(pref[2:]) + right
        return pref

def inverted_triple_array(nums):
    return 0

def modify_key(S, K):
    #remove dashes and uppercase everything
    # write your code in Python 3.6
    s_upper = S.upper()
    s_upper = s_upper.replace("-","")
        
    return_str = ""
    remainder =  len(s_upper)%K
    
    if len(s_upper)<=K:
        return S.upper()
    
    # elif remainder != 0:
    prev_i = 0
    for i in range(remainder, len(s_upper)+1, K):
        if i == 0:
            continue
        print(i)
        return_str += s_upper[prev_i:i] + '-'
        prev_i = i

    # else:
    #     for i in range(K, len(s_upper)+1, K):
    #         return_str += s_upper[:i] + '-'
    # if return_str[0] == '-':
    #     return_str = return_str[1:]
    return return_str[:-1]

def compare_time(time1, time2):
    """ for time format '23:59' """
    

    for i in range(5):
        if time1[i] == time2[i]:
            continue
        elif time1[i] > time2[i]:
            return 1
        else:
            return -1
    return 0

def next_time(time):
    digits = [time[0], time[1], time[3], time[4]]
    poss0 = [x for x in digits if x < '3']
    poss1 = [x for x in digits if x < '4']
    poss3 = [x for x in digits if x < '6']
    poss4 = digits

    permutations = []

    for i in range(len(poss0)):
        curr0 = poss0[i]
        poss1.remove(curr0)

        for j in range(len(poss1)):
            curr1 = poss1[j]
            poss3.remove(curr0)
            poss3.remove(curr1)

            for k in range(len(poss3)):
                curr3 = poss3[k]
                poss4.remove(curr0)
                poss4.remove(curr1)
                poss4.remove(curr3)

                for l in range(len(poss4)):
                    curr4 = poss4[l]
                    to_add = curr0+curr1+':'+curr3+curr4

                    if to_add not in permutations:
                        permutations.append(curr0+curr1+':'+curr3+curr4)

                poss4.append(curr0)
                poss4.append(curr1)
                poss4.append(curr3)

            poss3.append(curr0)
            poss3.append(curr1)

        poss1.append(curr0)
    
    if len(permutations) == 1:
        return permutations[0]

    time_above = '24:00'
    time_below = time
    return_time = time
    for perm in permutations:
        if compare_time(perm, time) == 1:
            if compare_time(perm,time_above) == -1:
                return_time = perm
                time_above = perm
        elif compare_time(perm, time) == -1:
            if compare_time(perm,time_below) == -1:
                time_below = perm
    
    if return_time == time:
        return time_below
    
    else:
        return return_time



def main():
    # ls = [4, 7, 0, 6, 9, 1, 5, 3, 8, 2]
    # print('ls is {}'.format(ls))
    # print('the sorted ls list is {}'.format(quicksort(ls)))

    # print(reverse32int(190))
    # print(reverse32int(-190))

    # print('the following is not recursive')
    # print(isnum_palindrome(121))
    # print(isnum_palindrome(9))
    # print(isnum_palindrome(-121))
    # print(isnum_palindrome(12345678987654321))
    # print(isnum_palindrome(12344321))
    # print(isnum_palindrome(1232321))
    # print(isnum_palindrome(12345))

    # print('the following is recursive')
    # print(isrec_numpalindrome(121))
    # print(isrec_numpalindrome(9))
    # print(isrec_numpalindrome(-121))
    # print(isrec_numpalindrome(12345678987654321))
    # print(isrec_numpalindrome(12344321))
    # print(isrec_numpalindrome(1232321))
    # print(isrec_numpalindrome(12345))

    # print(roman_to_int('IV'))
    # print(roman_to_int('VII'))
    # print(roman_to_int('IX'))
    # print(roman_to_int('MMMCMXCIX'))
    # print(roman_to_int('DCXXI'))

    # print(lcp_helper('hithere', 'hith3re'))
    # print(longest_common_prefix(['hithere', 'hith3re', 'hit']))
    # print(longest_common_prefix([""]))
    # print(longest_common_prefix(["caa","","a","acb"]))
    # print(valid_parentheses('['))
    # print(valid_parentheses(']'))
    # print(valid_parentheses('[])'))
    # linked_list1 = ListNode(1)
    # linked_list1.next = ListNode(2)
    # linked_list1.next.next = ListNode(4)

    # linked_list2 = ListNode(1)
    # linked_list2.next = ListNode(3)
    # linked_list2.next.next = ListNode(4)

    # print(linked_list1)
    # print(linked_list1.next)
    # print(linked_list2)

    # print(mergeTwoLists(linked_list1, linked_list2))
    # print(mergeTwoLists(linked_list1, linked_list2))
    # nums1 = [1, 1, 2, 2, 2, 3, 3, 3]
    # nums2 = [1,1,2]

    # print(remove_duplicates(nums1))
    # print(nums1)
    # print(remove_duplicates(nums2))
    # print(nums2)

    # nums = [3,4,3,4,3,3,4]
    # nums = [3, 2, 2, 3]
    # print(remove_element(nums,3))
    # print(nums)

    # hay = "hello"
    # needle = "ll"

    # print(needle_in_haystack(hay, needle))
    # arr1 = [1, 3, 5, 6]

    # print(search_insert_position(arr1, 5))
    # print(search_insert_position(arr1, 2))
    # print(search_insert_position(arr1, 7))
    # print(search_insert_position(arr1, 0))
    # print(countandsay(2))
    # print(countandsay(3))
    # print(countandsay(4))
    # print(countandsay(5))
    # print(countandsay(6))
    # print(countandsay(7))

    # print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    # print(max_subarray([-13, -3, 4,-1, 5, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]))

    # print(subarray_degree([2,1,1,3,2]))

    # print(length_of_lastword("Hello World"))
    # print(add_binary('1', '11'))

    # print(plus_one([9,9,9,9,9,9,9,9]))
    # print(common_restaurants(["Shogun", "Tapioca Express", "Burger King", "KFC"],["KFC", "Shogun", "Burger King"]))

    # arr = ["+1**23/14"]
    # arr2 = ["+*776"]
    # print(arr2)
    # print(prefix_to_suffix(arr2))

    # S = "2-4A0r7-4k"
    # print(modify_key(S, 4))

    print(next_time('11:00'))
    print(next_time('23:48'))
    print(next_time('23:00'))
    print(next_time('21:04'))

if __name__ == "__main__":
    main()
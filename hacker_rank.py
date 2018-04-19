from itertools import product
<<<<<<< HEAD
from collections import namedtuple
=======
import re
>>>>>>> ce8fa0c9ed50ec52986191db1fa8fbe96f5aae6a
# Helpers


# EASY
def weird_num():
    num = int(input("Input an integer: "))
    if num%2 == 0:
        if num in range(6,21):
            print('Weird')
        else:
            print('Not Weird')

    else:
        print('Weird')

def arithmetic():
    num1 = int(input("Input 1st integer: "))
    num2 = int(input("Input 2nd integer: "))

    print(num1+num2)
    print(num1-num2)
    print(num1*num2)


# MEDIUM

def minion_game(string):
    """
    Kevin counts substrings that begin with vowels. Stuart counts substrings 
    that begin with consonants. Returns the name and number of substrings that
    the maximum substring holder has.
    Input: String string
    Output: Prints name and score
    """
    vowels = 'AEIOU'
    kevin_pts = 0
    stuart_pts = 0
    str_len = len(string)
    for ind in range(str_len):
        if string[ind] in vowels:
            kevin_pts += str_len - ind
        else:
            stuart_pts += str_len - ind
    if kevin_pts > stuart_pts:
        print("Kevin {}".format(kevin_pts))
    elif stuart_pts > kevin_pts:
        print("Stuart {}".format(stuart_pts))
    else:
        print("Draw")

def merge_the_tools(string, k):
    """
    Splits string into k length segements containing only unique characters in 
    each segment.
    Input: String string, Integer k, where len(string) is divisible by k
    Output: Prints out unique character subsequences
    """
    prev_k = 0
    for end in range(k,len(string)+1, k):
        dict = {}
        print_str = ""
        for char in string[prev_k:end]:
            try:
                dict[char]
                pass
            except:
                dict[char] = 1
                print_str += char
        prev_k = end
        print(print_str)

def avg_marks():

    num_students = int(input())
    fields = input().split()
    total = 0

    students = namedtuple('Students', fields)
    for _ in range(num_students):
        field1, field2, field3, field4 = input().split()
        student = students(field1,field2, field3, field4)
        total += int(student.MARKS)

    print(total/int(num_students))

# HARD
# We can create wrappers for a lot of these functions!
def maximize_it():
    k, modulo = map(int,input("Input k and modulo base separated by space: ").split())

    # lol = []

    # for i in range(k):
    #     ls = map(int, list(input("Input numbers separated by spaces: ").split())[1:])
    #     # ls = [int(x) for x in ls]
    #     lol.append(ls)

    lol = list(map(int, list(input("Input numbers separated by spaces: ").split())[1:]) for _ in range(k))
    
    result_list = map(lambda x: sum(i**2 for i in x)%modulo, product(*lol))

    print(max(result_list))

# def valid_postal_code():
#     #add constraints of range 100000-999999
#     code = input("Input postal code: ")
#     counter = 0
#     for index in range(len(code)-2):
#         if(code[index]==code[index+2]):
#             counter +=1
#         if counter > 1:
#             print(False)
#             return

#     print(True)

def valid_postal_code():
    #SHOULD BE REGEX
    #add constraints of range 100000-999999
    code = input("Input postal code: ")
    counter = 0
    for index in range(len(code)-2):
        if(code[index]==code[index+2]):
            counter +=1
        if counter > 1:
            print(False)
            return

    print(True)
    # print(re.match(r'^' r'[1-4]\d{3}' r'$', input() ))
    # print(re.match(r'[0-9]\d{5}' r'$', input()))
    # print(re.match(r'[1-9]\d{5}$', '12324'))
    print(re.match(
    r'.*(.).\1.\1' r'[1-9]\d{5}', '213141'))
#     print(re.match(
#     r'^'
#     r'(?!.*(.).\1.*(.).\2)'
#     r'(?!.*(.)(.)\3\4)'
#     r'(?!.*(.).\5.\5)'  # This group
#     r'[1-9]\d{5}'
#     r'$', '101215'
# ))

def infix2postfix(expr):
    #can get rid of spaces using .split()
    precedence = {'*':2, '/':2, '+':1, '-':1, '(':0}
    operators = '()*/+-'
    stack = []
    return_exp = ''

    for index in range(len(expr)):
        if expr[index] not in operators:
            return_exp += expr[index]
        elif expr[index] == '(':
            stack.append('(')
        elif expr[index] == ')':
            while(True):
                stack_val = stack.pop()
                if stack_val == '(':
                    break
                else:
                    return_exp += stack_val
        else:
            while(len(stack)>0 and precedence[stack[-1]] >= precedence[expr[index]]):
                return_exp += stack.pop()
            stack.append(expr[index])
    while(len(stack)>0):
        return_exp += stack.pop()

    print(return_exp)
    # return return_exp

def infix2prefix(expr):
    #can get rid of spaces using .split()
    precedence = {'*':2, '/':2, '+':1, '-':1, ')':0}
    operators = '()*/+-'
    stack = []
    return_exp = ''

    for index in range(len(expr)-1,-1,-1):
        if expr[index] not in operators:
            return_exp += expr[index]
        elif expr[index] == ')':
            stack.append(')')
        elif expr[index] == '(':
            while(True):
                stack_val = stack.pop()
                if stack_val == ')':
                    break
                else:
                    return_exp += stack_val
        else:
            while(len(stack)>0 and precedence[stack[-1]] > precedence[expr[index]]):
                return_exp += stack.pop()
            stack.append(expr[index])
    while(len(stack)>0):
        return_exp += stack.pop()

    print(return_exp[::-1])

#my slightly incorrect definition
# def matrix_script():
#     n, m = input().strip().split(' ')
#     n, m = [int(n), int(m)]
#     matrix = []
#     matrix_i = 0
#     for matrix_i in range(n):
#         matrix_t = str(input().strip())
#         matrix_t += ' '*(m-len(matrix_t))
#         matrix.append(matrix_t)
        
#     ret_string = ''
#     for col in range(m):
#         for row in range(n):
#             ret_string += matrix[row][col]
            
#     matches = re.findall(r'[A-Za-z0-9]+([\$#%!]+ *)[A-Za-z0-9]', ret_string)
#     for match in matches:
#         ret_string = ret_string.replace(match, ' ')

#     print(ret_string)

#improved
def matrix_script():
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    matrix = []
    for _ in range(n):
        matrix.append(input())

    ret_str = ""
    for word in zip(*matrix):
        ret_str += "".join(word)

    print(re.sub(r'(?<=\w)([\W]+)(?=\w)', ' ', ret_str))

def main():
    # maximize_it()
    # valid_postal_code()
    # infix2postfix('A*(B+C)*D')
    infix2postfix('(A+B)*C-(D-E)*(F+G)')
    infix2prefix('(A+B)*C-(D-E)*(F+G)')

if __name__ == "__main__":
    main()
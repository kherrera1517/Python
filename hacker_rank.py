from itertools import product
import re
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
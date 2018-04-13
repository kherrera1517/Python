from itertools import product
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

def valid_postal_code():
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

def main():
    # maximize_it()
    valid_postal_code()

if __name__ == "__main__":
    main()
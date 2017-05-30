from primality import trial_division

def primelist(n):
    if n > 0:
        print(2)
        if n > 1:
            print(3)
            if n > 2:
                y = 6
                x = 0
                for i in range(1,n-1):
                    if i%2 == 1:
                        x += y
                        if trial_division(x-1):  
                            print(x-1)
                    if i%2 == 0:
                        if trial_division(x+1):
                            print(x+1)
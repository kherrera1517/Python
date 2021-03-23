def multiplesof(start, multiplicand, upto, filter=1):
    lofBeats=[start]
    for factor in range(1,upto+1):
        lofBeats.append(start+multiplicand*factor)
    if filter != 1:
        print(start)
    for index in range(len(lofBeats)):
        if((index+1)%filter==0):
            print(lofBeats[index])
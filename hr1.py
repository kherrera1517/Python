def can_reach(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return True
    elif x1 < x2 and y1 == y2:
        return can_reach(x1+y1,y1,x2,y2)
    elif y1 < y2 and x1 == x2:
        return can_reach(x1,y1+x1,x2,y2)

    elif x1 < x2 and y1 < y2:
        return can_reach(x1+y1, y1, x2, y2) or can_reach(x1,y1+x1,x2,y2)

    return False

def points_belong_to_triangle(x1, y1, x2, y2, x3, y3, xP, yP, xQ, yQ):
    if x1 == x2 == x3:
        return 0
    #have to add case for vertical line made by two points
    slope1_2 = (y2-y1)/(x2/x1)
    slope1_3 = (y3-y1)/(x3/x1)
    slope2_3 = (y3-y2)/(x3/x2)

    if slope1_2 == slope1_3 == slope2_3:
        return 0

    b1 = -1*slope1_2*x1+y1
    b2 = -1*slope1_3*x1+y1
    b3 = -1*slope2_3*x2+y2
    

    line1_2 = lambda x: slope1_2*x+b1
    line1_3 = lambda x: slope1_3*x+b2
    line2_3 = lambda x: slope2_3*x+b3


def main():

    return

if __name__ == "__main__":
    main()
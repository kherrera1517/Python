def play(tree):
    # print(tree[0])
    # print("Please answer 'yes' or 'no'!")
    if tree[1] is None:
        answer = input("Is it " + tree[0] + "?\n")
        
        if answer == "yes":
            print("YAY I GOT IT!")

        if answer == "no":
            correct = input("Darn! What was it?\n")
            new_question = input("What's a question that distinguishes between "\
             + tree[0])
    answer = input(tree[0] + "\n")
    if answer == "yes":
        return play(tree[1])
    else:
        return play(tree[2])



[ “cat”, dog, moose, elephant, dog, moose, dog, giraffe ] -> 1

def repeat(lst):
    for i in range(len(lst)-1):
        if lst[i] in lst[i+1:]:
            return i
    
    return None


def repeat(lst):
    seen = {}
    smallest = len(lst)
    for i in range(len(lst)):
        if lst[i] in seen:
           if seen[lst[i]] < smallest:
               smallest = seen[lst[i]]
	 seen[lst[i]] = i
    
    if smallest == len(lst):
        return None
    
    return smallest

def lastRepeating(lst):
    seen = {}
    recent = None
    for i in range(len(lst)):
        if lst[i] in seen:
            recent = i
        seen[lst[i]] = i

    return recent

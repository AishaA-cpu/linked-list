# Given two integers m and n, loop repeatedly through an array of m and remove each nth element. Return the last element left
# (If m = 7 and n = 4, then begin with the array 1 2 3 4 5 6 7 and remove, in order, 4 1 6 5 2 7 and return 3.)

m = 7
n = 4

# remove 4th element 
# continue from the element in front of the position that was popped 
# remove next 4th 

def recursion(elem, n):
    start = elem[n::]
    end = elem[0:n-1:]
    start += end

    
    if len(elem) == 1:
        #print(elem[0])
        return elem[0]           # Terminate recursion
    elif len(elem) == 2:
        return recursion(elem[0:1], 0)
    elif len(elem) > 4:
        recursion(start, n)
    else:        
        # print(end)
        return recursion(start, len(elem) - 2)


    

test = recursion([1, 2, 3, 4, 5, 6, 7], 4)

print(test)
#Question 1.4
def IsPalindrome ( S ) :
    #Does the sequence 'S' read the same forewards and backwards?
    start = 0
    end = len ( S ) -1
    while start < end :
        if S [start] != S [end] :
            return False
        start +=1
        end -= 1
            
    return True
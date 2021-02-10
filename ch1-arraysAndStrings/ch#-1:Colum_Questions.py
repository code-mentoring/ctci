# Question 1.1 - Is Unique


def IsUnique( S ):
    for i in range(len( S )):
        for j in range(i + 1, len( S )):
            if(S[i] == S[j]):
                return False
    return True

# Question 1.2 - Check Permutation


def IsPermutation( S1, S2 ):
    LenS1 = len( S1 )
    LenS2 = len( S2 )
    if (LenS1 != LenS2 ):
        return False
    SorS1 = sorted( S1 )
    S1 = " ".join( SorS1 )
    SorS2 = sorted( S2 )
    S2 = " ".join( SorS2 )
    for i in range(0, LenS1, 1):
        if ( S1[i] != S2[i] ):
            return False
    return True

# Question 1.4 - Palindrome Permutation


def IsPalindrome( S ):
    start = 0
    end = len( S ) - 1
    while start < end:
        if S[start] != S[end]:
            return False
        start += 1
        end -= 1

    return True

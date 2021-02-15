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

"""
Shane Sheridan's solution to question 1.4 Palindrome Permutation
My Solution above does not cover all case scenarios.
"""
def is_palindrome_permutation(s):
    # Palindromes ignore punctuation, spaces and case. E.g. 'No lemon, no melon'.
    s = remove_punctuation(s)
    
    length = len(s)
    if (length <= 1):
        return False
    
    # If each character occurs even number of times, then it must be a palindrome.
    # Except odd length palindromes which must have one extra character, i.e. the middle.
    is_even_length = is_even(length)
    found_odd_count = False
    for c in s:
        count = get_occurrences(c, s)
        even_occurrence = is_even(count)
        if (is_even_length and not(even_occurrence)):
             return False
        elif (not(is_even_length) and not(even_occurrence)):
            # Allow for one extra character in odd length strings.
            if (found_odd_count):
                return False
            else:
                found_odd_count = True

    return True

def is_even(num):
    return (num % 2 == 0)

def get_occurrences(c, s):
    count = 0
    for i in s:
        if i == c:
            count += 1
    
    return count
    
def remove_punctuation(s):
    # Removing '/' and including ' ' in python's built in 'string.punctuation'.
    punctuation = r"""!"#$%&'()*+,-.:;<=>?@[\]^_`{|}~ """
    for c in s:
        if c in punctuation:
            s = s.replace(c, "")

    return s.lower()

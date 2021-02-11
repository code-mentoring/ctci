# 1.4 - Palindrome Permutation 
# Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.
#
# Palindromes ignore punctuation, spaces and case. E.g. 'no lemon, no melon'.
   
# Take string, find each permutation of it, for each permutation check if palindrome.

# Check for palindrome using recursive algorithm with 3 base cases and recursive
# call passing the same string minus its first and last characters.
def is_palindrome(s):
    #print(f"Checking string: {s}")
    s = remove_punctuation(s)
    
    length = len(s)
    if (length == 1):
        # Odd length palindromes end here.
        return True
    elif (length == 2): 
        # Even length palindromes end here.
        return (s[0] == s[1])
    elif (s[0] != s[length-1]):
        # Non-palindrome strings end here.
        return False
    else:
        # Remove first and last char since these are checked above, and recur.
        return is_palindrome(s[1:-1])

def remove_punctuation(s):
    punctuation = r"""!"#$%&'()*+,-.:;<=>?@[\]^_`{|}~ """
    for c in s:
        if c in punctuation:
            s = s.replace(c, "")
    
    return s
   
    
# Testing. 
 
# Palindromes: 'madam', 'racecar', '11/11/11', 'no lemon, no melon'
#some_strings = ["aa", "ab", "abc", "aba", "madam", "anzana", "racecar", "11/11/11", "no lemon, no melon", "an I'm a tuna", "123421", "he!!0"]
#for s in some_strings:
#    print(f"Checking if '{s}' is a palindrome.")
#    print(is_palindrome(s)) 
    
some_strings = ["apple", "banana", "cherry", "tuna", "12345", "123445", "he!!0", "he123", "he1233", "he rt", "h tr s"]
#for s in some_strings:
    #print(f"Checking if '{s}' is a permutation of a palindrome.")
    #print(is_palindrome_permutation(s)) 
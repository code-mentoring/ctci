# 1.4 - Palindrome Permutation 
# Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters. 
# The palindrome does not need to be limited to just dictionary words.
   
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
   
    
# Testing.  
some_strings = ["aa", "ab", "abc", "aba", "madam", "anzana", "racecar", "raeccar", "11/11/11", 
                "No lemon, no melon", "an I'm a tuna", "123421", "he!!0", "taco tac"]
for s in some_strings:
    print(f"Checking if '{s}' is a permutation of a palindrome.")
    print(is_palindrome_permutation(s)) 
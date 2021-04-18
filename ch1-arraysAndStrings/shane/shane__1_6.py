# 1.6 - String Compression.
# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string 'a a b c c c c c a a a' would become 'a 2 b l c 5 a 3'.
# If the "compressed" string would not become smaller than the original string, your method should
# return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

# Group duplicate characters and build compressed string using each char plus
# group size. Ignoring spaces since string has only uppercase and lowercase letters.
def compress_string(original_string):
    original_length = len(original_string)
    if (original_length <= 2): 
        # Cannot compress any smaller.
        return original_string
    
    duplicate_groups = split_duplicate_groups(original_string)

    print(f"string_array: {duplicate_groups}")

    compressed_string = ''
    for group in duplicate_groups:
        duplicate_char = group[0]
        count = len(group)
        compressed_string += (duplicate_char + str(count))

    print(f"compressed_string: {compressed_string}")    

    is_compressed_smaller = (original_length > len(compressed_string))
    return compressed_string if (is_compressed_smaller) else original_string

def split_duplicate_groups(input_string):
    length = len(input_string)
    duplicate_groups = []
    previous = input_string[0]
    previous_index = 0
    for i in range(length-1):
        i += 1 # Skip first char.

        current = input_string[i]
        if (current != previous):
            duplicate_groups.append(input_string[previous_index:i])
            previous_index = i

        is_last_char = i == (length-1)    
        if (is_last_char): 
            duplicate_groups.append(input_string[previous_index:])

        previous = current

    return duplicate_groups

# Testing.  
some_strings = ["a", "ab", "aa", "aaab", "aaabbbccaaa", "aaabb bc caaa", "aAAbbbccAaa", "aaabbbccaaa"]
for s in some_strings:
    print(f"Compressing '{s}' to: ")
    print(f"'{compress_string(s)}'. ")
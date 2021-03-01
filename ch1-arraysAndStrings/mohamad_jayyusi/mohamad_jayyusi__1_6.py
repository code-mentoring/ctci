# /**
#  * @author [Mohamad Jayyusi]
#  * @email 
#  * @create date 2021-02-23
#  * @modify date 2021-02-23
#  * @desc # 1.6 - String Compression:
# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string a a b c c c c c a a a would become a 2 b 1 c 5 a 3 , If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
#  */


#O(n²)
def compress(text):
    result = ""
    i=0
    while(i < len(text)):
        count = 1
        for j in range(i+1,len(text)):
            if(text[i] == text[j]):
                count = count+1
            else:
                break
        result = result + text[i] + str(count)
        i = i + count
    return result if len(result) < len(text) else text

tests = [ 
"aabcccccaaa", 
"abc",
"aabc",
"bc",
"a",
"aaaa",
"aaaaac",
"aba",
"abcc",
"",
]

results = [
"a2b1c5a3",
"abc",
"aabc",
"bc",
"a",
"a4",
"a5c1",
"aba",
"abcc",
"",
]

for i in range(0,len(tests)):
    if( results[i] == compress(tests[i])):
        print("PASS")
    else:
        print("*FAIL*")
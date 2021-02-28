"""
1.6 - String Compression:
Implement a method to perform basic string compression using the counts of repeated characters. For example, the string a a b c c c c c a a a would become a 2 b 1 c 5 a 3 , If the "compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

def compress(s):
    counts = []
    i = 0
    while i < len(s):
        current = s[i]
        j = i+1
        while j < len(s) and s[j] == current:
            j += 1
        counts.append((current, j-i))
        i = j
    new_s = "".join(f"{c}{count}" for c, count in counts)
    if len(new_s) < len(s):
        return new_s
    return s

def main():
    cases = [
        ("", ""),
        ("a", "a"),
        ("aa", "aa"),
        ("aaa", "a3"),
        ("ab", "ab"),
        ("aaabbb", "a3b3"),
        ("abbbb", "a1b4")

    ]
    for s, expected in cases:
        actual = compress(s)
        print("[" + ("PASS" if actual == expected else "FAIL") + "]",
              s,
              expected,
              actual)

if __name__ == "__main__":
    main()

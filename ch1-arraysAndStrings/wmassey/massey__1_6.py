#!/usr/bin/env python3
"""project: Cracking the Coding Interview: Chapter 1; Strings & Arrays 
created:2021-09-25, @author:Will Massey, email: wmassey776@gmail.com

Objective:
    String Compression: Implement a method to perform basic string compression using the counts
    of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
    "compressed" string would not become smaller than the original string, your method should return
    the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

def solve(s):
    comp_s = ''
    count = 1
    for i in range(len(s) -1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            comp_s += s[i] + str(count)
            count = 1
    comp_s += s[i] + str(count)

    if len(comp_s) >= len(s):
        return s
    else:
        return comp_s


def main():
    print(solve('aabcccccaaa'))


if __name__ == '__main__':
    main() 

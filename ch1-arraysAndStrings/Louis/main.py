
def is_unique(s):

    checked = []

    for i in s:
        if i in checked:
            return True
        else:
            checked.append(i)
    return False

def check_permutation(s,t):

    sortedA = sorted(s)
    sortedB = sorted(t)

    if sortedA == sortedB:
        return True
    else:
        return False

def palindrome_permutation(s):
    s = s.lower()
    s = s.replace(" ", "")

    checked = []

    for i in s:
        if i in checked:
            checked.remove(i)
        else:
            checked.append(i)

    if len(checked) == 1:
        return True
    else:
        return False






if __name__ == "__main__":
    print(is_unique(s="Helo"))
    print(check_permutation(s="man",t="nma"))

    print(palindrome_permutation(s="Tact Coa"))

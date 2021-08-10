#exercise session 1
def isUnique(s):

    check = []

    for i in s:
        if i in check:
            return False
        else:
            check.append(i)
    return True


def permutation(a,b):
    sortedA = sorted(a)
    sortedB = sorted(b)


    if sortedA == sortedB:
        return True
    else:
        return False

def palindrome_permutation(s):

    s = s.replace(" ","")
    s = s.lower()

    check = []

    for i in s:
        if i in check:
            check.remove(i)
        else:
            check.append(i)

    print(len(check))

    if len(check) == 1:
        return True
    else:
        return False






if __name__ == "__main__":
    a = 'Tact Coa'

    print(palindrome_permutation(a))
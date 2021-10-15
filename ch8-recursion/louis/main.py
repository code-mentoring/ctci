#sorted_array: the array in which we are going to find the magic index


def magic_index(sorted_array,s,e):

    if s<=e:
        m = int(s+e) //2
        

    if m==sorted_array[m]:
        return m

    if m > sorted_array[m]:
        return magic_index(sorted_array,m+1,e)
    else:
        return magic_index(sorted_array,s,m-1)
















if __name__ == "__main__":
    a = [-10,-5,0,1,4,20]
    print(magic_index(a,0,len(a)))
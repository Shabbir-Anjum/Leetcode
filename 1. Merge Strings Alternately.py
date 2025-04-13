def main(w1,w2):
    merge=[]
    i,j=0,0
    len1,len2=len(w1),len(w2)
    while i<len1 and j<len2:
        merge.append(w1[i])
        merge.append(w2[j])
        i+=1
        j+=1
    if i<len1:
        merge.extend(w1[:i])
    elif j<len2:
        merge.extend(w2[:j])
    return "".join(merge)
print(main('abcd','ef'))
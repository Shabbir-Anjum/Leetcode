def main(str, n):
    count=0
    length=len(str)
    for i in range(length):
        if str[i]==0:
            left= (i==0) or (str[i-1]==0)
            right= (i==length-1) or (str[i+1]==0)
            if left and right:
                str[i]=1
                count+=1
        if count>=n:
            return True
    return count>=n
print(main([1,0,0,0,0,1,0,1], 1))
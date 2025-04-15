def candies(cand, left_cand):
    result=[]
    maximum=max(cand)
    for candy in cand:
        result.append(candy + left_cand >= maximum)
    return result
print(candies([1,6,9,4,5],6))
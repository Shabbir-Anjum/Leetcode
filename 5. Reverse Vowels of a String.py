def main(a):
    words=a.split()
    result=words[::-1]
    return " ".join(result)
print(main("the sky is blue"))
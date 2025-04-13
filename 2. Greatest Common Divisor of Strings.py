def my_gcd(a,b):
    while b !=0:
        a,b=b,a % b
    return a
def main(s1,s2):
    if s1 + s2 != s2 + s1:
        return ""
    gcd_len= my_gcd(len(s1), len(s2))
    return s1[:gcd_len]
print(main("ab","abababab"))
# number : 16
# increment and decrement by 5
# 16 11 6 1 -4 1 6 11 16
#How to print above pattern without any extra variable and loop?
def pattern(n):
    if n == 0 or n < 0:
        print(n, end=", ")
        return
    print(n,end=", ")
    pattern(n-5)
    
    print(n, end=", ")

pattern(16)   

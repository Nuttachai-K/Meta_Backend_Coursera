import time

str = 'racecar'

def isPalindrome(str):
    for i in range(int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

def isPalindrome2(str):
    startIndex = 0
    endIndex = len(str) -1

    for i in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True

t1 = time.time()
#print(isPalindrome(str)) #0.0009973049 0.0006341934
print(isPalindrome2(str)) #0.0009629726 0.0009059906
t2 = time.time()
print(round(t2-t1,10))

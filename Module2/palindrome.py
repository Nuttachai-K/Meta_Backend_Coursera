
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

print(isPalindrome2(str))

#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twosum(a, target):

    for i in range(len(a)):
        for j in range(1, len(a)):
            if a[j] == target - a[i]:
               print ('[ '+str(i)+ ', '+str(j)+']')

#####################################################################################

def lengthOfLongestSubsequence(s):
    result = ""
    for i in range(len(s)):
        if s[i] in result:
            continue
        else:
            result += s[i]

    return result

#####################################################################################

def lengthOfLongestSubstring(s):

    listStr = []
    for i in range(len(s)):
        result = ""
        for j in range(i, len(s)):
            if s[j] == s[j-1] or s[j] in result:
                break;
            else:
                result += s[j]
        listStr.append(result)

    print("maximum element in list", max(listStr, key=len))
    return listStr

#####################################################################################

def longestPalindrome(s):

    listOfStrings = []
    for i in range(len(s)):
        ns = ""
        for j in range(i, len(s)):
            ns += s[j]
            listOfStrings.append(ns)

    print(listOfStrings)

    listOfPalindromes = []

    for string in listOfStrings:
        if isPalindrome(string):
            listOfPalindromes.append(string)

    print(max(listOfPalindromes, key=len))
    return listOfPalindromes


def isPalindrome(str):
        i = 0
        j = len(str) - 1
        while i <= j:
            if str[i] != str[j]:
                return False
            i += 1
            j -= 1
        return True

###############################################################################################

def strZigZag(s, rows):
    newStr = ""
    newStr += s[0]
    while rows > 0:
        for i in range(len(s)):
            if i+rows <= len(s):
                newStr += s[rows]
                print(newStr)

        rows -= 1
    return newStr

def addSum(nums, target):
    listOfCombs = []
    size = len(nums)
    for i in range(len(nums)):
        if 1 in nums:
            combs = []
            while size:
                combs.append(2)
                size -= 1
            listOfCombs.append(combs)
        elif 2 in nums and target % 2 == 0:
            combs = []
            while size:
                combs.append(2)
                size += 2
            listOfCombs.append(combs)

###################################################################################################33

def sumCheck(arr, target):
    listOfSums = []
    for i in range(len(arr)):
        if arr[i] == target:
            print('hi')
            listOfSums.append(target)
        if arr[i] < target :
            if arr[i] == 1 :
                for j in range(target):
                    listOfSums.append(1)
            else:
                if target % arr[i] == 0 :
                    quotient = target // arr[i]
                    for k in range(quotient):
                        listOfSums.append(arr[i])

                elif target - arr[i] in arr:
                    listOfSums.append(arr[i])
                    listOfSums.append(target - arr[i])
    return listOfSums


def main():

   # print(twosum([3, 7, 4, 15, 0, 5, 2], 7))
    #print('subsequence : ', lengthOfLongestSubsequence("abcabbdcf"))
    #print('substring: ', lengthOfLongestSubstring("abcdabcdefbb"))
    #print('substring2: ', longestSubString("abcabbdcf"))
    #print(longestPalindrome('agbabgbb'))
    #print(strZigZag('PAYPALISHIRING', 3))
    #print(isPalindrome('aba'))
    print(sumCheck([1,2,3,4,5,6], 6))

if __name__ == '__main__':
    main()

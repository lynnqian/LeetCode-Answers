# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# 633. Sum of Square Numbers
# inspiration from discussion: take the square root of c to eliminate the time required
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(c ** 0.5)
        while l <= r:
            left_side = l ** 2 + r ** 2
            if left_side == c:
                return True
            if left_side < c:
                l += 1
            else:
                r -= 1

        return False

# 680. Valid Palindrome II
# from discussion
class Solution:
    class Solution:
        def validPalindrome(self, s: str) -> bool:
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                if s[i] != s[j]:
                    return self.helper(s, i + 1, j) or self.helper(s, i, j - 1)
            return True

        def helper(self, s, i: str, j: str) -> bool:
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

# 524. Longest Word in Dictionary through Deleting
# first solution: slow. 580ms
class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        length = 0
        returnValue = ""
        for value in dictionary:
            if len(value) < length:
                continue
            if self.isInS(s, value):
                if len(value) > length:
                    returnValue = value
                    length = len(value)
                elif len(value) == length:
                    if value < returnValue:
                        returnValue = value
        return returnValue

    def isInS(self, s, value):
        startS = 0
        startV = 0
        while startS < len(s):
            if s[startS] == value[startV]:
                startV += 1
            startS += 1
            if startV == len(value):
                return True
        return False

# second solution: from discussion
    def findLongestWord(self, s, d):
        def isSubsequence(x):
            it = iter(s)
            return all(c in it for c in x)

        return min(filter(isSubsequence, d) + [''], key=lambda x: (-len(x), x))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hello");
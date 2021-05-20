
# 452: Minimum Number of Arrows to Burst Balloons
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key = lambda points: points[1])
        begin = points[0][0]
        end = points[0][1]
        count = 1
        for i in range(len(points)):
            if points[i][0] > end:
                begin = points[i][0]
                end = points[i][1]
                count += 1
                continue
            if begin > points[i][0]:
                continue
            else:
                begin = points[i][0]
        return count

# 763. Partition Labels
class Solution:
    def partitionLabels(self, S: str) -> list[int]:
        returnedList = []
        indexPositionList = {}
        for x in range(0, len(S)):
            if S[x] not in indexPositionList:
                # record the start position and the end appearance of this letter
                indexPositionList[S[x]] = [x, x]
            else:
                indexPositionList[S[x]][1] = x
        currentMax = indexPositionList[S[0]][1]
        current_index = 0
        last_current_max = -1
        for value in S:
            if indexPositionList[value][1] > currentMax:
                currentMax = indexPositionList[value][1]
            # if reaching the end, then append
            if current_index == len(S) - 1:
                returnedList.append(currentMax - last_current_max)
                break
            elif current_index == currentMax:
                returnedList.append(currentMax - last_current_max)
                last_current_max = currentMax
                currentMax = indexPositionList[value][1]
            current_index += 1
        return returnedList

    #solution from Leetcode:
    class Solution(object):
        def partitionLabels(self, S):
            last = {c: i for i, c in enumerate(S)}
            j = anchor = 0
            ans = []
            for i, c in enumerate(S):
                j = max(j, last[c])
                if i == j:
                    ans.append(i - anchor + 1)
                    anchor = i + 1

            return ans


# 122. Best Time to Buy and Sell Stock II
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxValue = 0
        current_max = 0
        current_min = prices[0]
        for i in range(0, len(prices) - 1):
            if prices[i] > prices[i + 1]:
                maxValue += current_max
                current_max = 0
                current_min = prices[i + 1]
            elif prices[i] < prices[i + 1]:
                current_max = prices[i + 1] - current_min
            # check if we have reached the end
            if i + 2 == len(prices):
                maxValue += current_max
                break
        return maxValue

    # or you could just add the ones that are up-hill! much simpler.

# 406. Queue Reconstruction by Height
class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:



# 665. Non-decreasing Array
# from discussion
class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if count or (i > 1 and i < len(nums) - 1 and nums[i - 2] > nums[i] and nums[i + 1] < nums[i - 1]):
                    return False
                count = 1
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hi")
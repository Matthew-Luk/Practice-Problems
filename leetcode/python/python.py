# 1929. Concatenation of Array
class Solution:
    def getConcatenation(self, nums):
        return nums + nums

# 2469. Convert the Temperature
class Solution:
    def convertTemperature(self, celsius):
        return [(celsius+273.15),(celsius * 1.80 + 32.00)]

# 2235. Add Two Integers
class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

# 1108. Defanging an IP Address
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

# 1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums):
        x = 0
        for i in range(len(nums)):
            x += nums[i]
            nums[i] = x
        return nums

# 2011. Final Value of Variable After Performing Operations
class Solution:
    def finalValueAfterOperations(self, operations):
        x = 0
        for i in operations:
            if i.count("++") > 0:
                x += 1
            else:
                x -=1
        return x
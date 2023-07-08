from typing import List, Optional, ListNode
import math

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

# 1512. Number of Good Pairs
class Solution:
    def numIdenticalPairs(self, nums):
        counter = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    counter += 1
        return counter

# 1672. Richest Customer Wealth
class Solution:
    def maximumWealth(self, accounts):
        for i in range(len(accounts)):
            accounts[i] = sum(accounts[i])
        return max(accounts)

# 771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels, stones):
        jewels = [ch for ch in jewels]
        stones = [ch for ch in stones]
        x = 0
        for i in range(len(jewels)):
            for j in range(len(stones)):
                if jewels[i] == stones[j]:
                    x += 1
        return x

# 2413. Smallest Even Multiple
class Solution:
    def smallestEvenMultiple(self, n):
        if n % 2 == 0:
            return n
        else:
            return 2 * n

# 2114. Maximum Number of Words Found in Sentences
class Solution:
    def mostWordsFound(self, sentences):
        for i in range(len(sentences)):
            sentences[i] = (sentences[i].count(" ") + 1)
        return max(sentences)

# 1920. Build Array from Permutation
class Solution:
    def buildArray(self, nums):
        ans = [0] * len(nums)
        for i in range(len(ans)):
            ans[i] = nums[nums[i]]
        print(ans)
        return ans

# 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        x = max(candies)
        print (f"The max is: {x}")
        for i in range(len(candies)):
            if candies[i] + extraCandies >= x:
                candies[i] = True
            else:
                candies[i] = False
        print(f"This is the print statement: {candies}")
        return(candies)

# 1281. Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = [int(d) for d in str(n)]
        product = 1
        for i in range(len(n)):
            product *= n[i]
        return product - sum(n)

# 1365. How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        y = []
        for i in range(len(nums)):
            x = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    x += 1
            y.append(x)
        return y

# 1662. Check If Two String Arrays are Equivalent
class Solution:
    def arrayStringsAreEqual(self, word1, word2):
        x = ""
        y = ""
        for i in range(len(word1)):
            x += word1[i]
        for i in range(len(word2)):
            y += word2[i]
        return x == y

# 2236. Root Equals Sum of Children
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def checkTree(self, root):
        return(root.val == root.left.val + root.right.val)

# 1678. Goal Parser Interpretation
class Solution:
    def interpret(self, command):
        command = command.replace("()","o")
        command = command.replace("(al)","al")
        return command

# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums, n):
        nums2 = nums[0:n]
        nums3 = nums[n:]
        x = []
        for i in range(len(nums2)):
            x.append(nums2[i])
            x.append(nums3[i])
        return x

# 1389. Create Target Array in the Given Order
class Solution:
    def createTargetArray(self, nums, index):
        target = []
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target

# 1832. Check if the Sentence Is Pangram
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for i in alphabet:
            if i not in sentence.lower():
                return False
        return True

# 1773. Count Items Matching a Rule
class Solution:
    def countMatches(self, items, ruleKey, ruleValue):
        x = 0
        y = 0
        if ruleKey == "color":
            y = 1
        elif ruleKey == "name":
            y = 2
        for i in range(len(items)):
            if items[i][y] == ruleValue:
                print(items[i][0])
                x += 1
        return x

# 2160. Minimum Sum of Four Digit Number After Splitting Digits
class Solution:
    def minimumSum(self, num: int) -> int:
        new1 = []
        new2 = []
        num = [int(x) for x in str(num)]
        num.sort()
        new1.append(num[0])
        new2.append(num[1])
        num.pop(0)
        num.pop(0)
        if new1[0] >= new2[0]:
            new2.append(num[0])
            new1.append(num[1])
        else:
            new1.append(num[0])
            new2.append(num[1])
        num.pop(0)
        num.pop(0)
        new1 = [str(x) for x in new1]
        new2 = [str(x) for x in new2]
        new1 = "".join(new1)
        new2 = "".join(new2)
        print(new1)
        print(new2)
        return (int(new1) + int(new2))

# 1859. Sorting the Sentence
class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        x = [""] * len(s)
        for word in s:
            index = word[-1]
            x[(int(index)-1)] = word[:-1]
        return " ".join(x)

# 1528. Shuffle String
class Solution:
    def restoreString(self, s, indices):
        x = [""] * len(s)
        for i in range(len(s)):
            x[indices[i]] = s[i]
        return "".join(x)

# 1816. Truncate Sentence
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        return " ".join(s[:k])

# 2006. Count Number of Pairs With Absolute Difference K
class Solution:
    def countKDifference(self, nums, k):
        x = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(abs(nums[i] - nums[j]) == k):
                    x += 1
        return x

# 2315. Count Asterisks
class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0
        s = s.split("|")
        for i in range(len(s)):
            if i % 2 == 0:
                for char in s[i]:
                    if char == "*":
                        count += 1
        return count

# 1323. Maximum 69 Number
class Solution:
    def maximum69Number (self, num: int) -> int:
        num2 = []
        count = 0
        for i in str(num):
            if i == "9":
                num2.append(i)
            elif i == "6" and count == 0:
                num2.append("9")
                count = 1
            else:
                num2.append(i)
        return int("".join(num2))

# 709. To Lower Case
class Solution:
    def toLowerCase(self, s: str) -> str:
        s = [char for char in s]
        for i in range(len(s)):
            if s[i].isupper():
                s[i] = s[i].lower()
        return "".join(s)

# 557. Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        newWord = []
        for i in range(len(s)):
            for j in range(len(s[i])-1,-1,-1):
                newWord.append(s[i][j])
            newWord.append(" ")
        return "".join(newWord[:-1])

# 1684. Count the Number of Consistent Strings
class Solution:
    def countConsistentStrings(self, allowed, words):
        count = len(words)
        cache = set(allowed)
        for i in range(len(words)):
            for char in range(len(words[i])):
                if words[i][char] not in cache:
                    count -= 1
                    break
        return count

# 832. Flipping an Image
class Solution:
    def flipAndInvertImage(self, image):
        newArray = []
        for i in range(len(image)):
            temp = []
            for j in range(len(image[i])-1,-1,-1):
                if image[i][j] == 1:
                    temp.append(0)
                else:
                    temp.append(1)
            newArray.append(temp)
        return(newArray)

# 1913. Maximum Product Difference Between Two Pairs
class Solution:
    def maxProductDifference(self, nums):
        newNums = sorted(nums)
        return((newNums[-1] * newNums[-2]) - (newNums[0] * newNums[1]))

# 2037. Minimum Number of Moves to Seat Everyone
class Solution:
    def minMovesToSeat(self, seats, students):
        seats = sorted(seats)
        students = sorted(students)
        count = 0
        for i in range(len(seats)):
            count += abs(seats[i] - students[i])
        return count

# 2176. Count Equal and Divisible Pairs in an Array
class Solution:
    def countPairs(self, nums, k):
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    if (i * j) % k == 0:
                        count += 1
        return count

# 2427. Number of Common Factors
class Solution:
    def commonFactors(self, a, b):
        count = 0
        for i in range(1,a+1):
            if a % i == 0 and b % i == 0:
                count += 1
        return count

# 1844. Replace All Digits with Characters
class Solution:
    def replaceDigits(self, s: str) -> str:
        x = []
        for i in range(len(s)):
            if i % 2 != 0:
                x.append(chr(ord(s[i-1]) + int(s[i])))
            else:
                x.append(s[i])
        return "".join(x)

# 1464. Maximum Product of Two Elements in an Array
class Solution:
    def maxProduct(self, nums):
        newNums = sorted(nums)
        return (newNums[-1] - 1) * (newNums[-2] - 1)

# 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain):
        x = [0]
        for i in gain:
            x.append(x[-1] + i)
        return(max(x))

# 1295. Find Numbers with Even Number of Digits
class Solution:
    def findNumbers(self, nums):
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                count += 1
        return count

# 1313. Decompress Run-Length Encoded List
class Solution:
    def decompressRLElist(self, nums):
        results = []
        for i in range(len(nums)):
            if i % 2 != 0:
                count = nums[i-1]
                while(count > 0):
                    results.append(nums[i])
                    count -= 1
        return(results)

# 1342. Number of Steps to Reduce a Number to Zero
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while(num > 0):
            if num % 2 == 0:
                num = num / 2
                count += 1
            else:
                num -= 1
                count += 1
        return count

# 2194. Cells in a Range on an Excel Sheet
class Solution:
    def cellsInRange(self, s):
        results = []
        s = s.split(":")
        for i in range(ord(s[0][0]),ord(s[1][0])+1):
            for j in range(ord(s[0][1]),ord(s[1][1])+1):
                temp = []
                temp.append(chr(i))
                temp.append(chr(j))
                results.append("".join(temp))
        return(results)

# 2185. Counting Words With a Given Prefix
class Solution:
    def prefixCount(self, words, pref):
        count = 0
        length = len(pref)
        print(length)
        for i in words:
            if i[:length] == pref:
                count += 1
        return count

# 2000. Reverse Prefix of Word
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = 0
        results = []
        for i in range(len(word)):
            if word[i] == ch:
                index = i
                break
        pref = (word[:index+1])
        for i in range(len(pref)-1,-1,-1):
            results.append(pref[i])
        results.append(word[index+1:])
        return("".join(results))

# 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums) -> int:
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count == sum(nums[i:]):
                return i
        return -1

# 217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums) -> bool:
        return len(nums) != len(set(nums))

# 704. Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (high + low) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

# 977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums):
        return sorted([i * i for i in nums])

# 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums) -> None:
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

# 344. Reverse String
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left <= right:
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            left += 1
            right -= 1

# 1. Two Sum
class Solution:
    def twoSum(self, nums, target: int):
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result

# 2520. Count the Digits That Divide a Number
class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        x = [int(i) for i in str(num)]
        for i in range(len(x)):
            if num % x[i] == 0:
                count += 1
        return count

# 1688. Count of Matches in Tournament
class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while(n>1):
            if n % 2 == 0:
                n = n/2
                count += n
            else:
                n = n//2
                count += 1
                count += n
        return int(count)

# 2535. Difference Between Element Sum and Digit Sum of an Array
class Solution:
    def differenceOfSum(self, nums) -> int:
        element = sum(nums)
        digit = 0
        for i in range(len(nums)):
            if nums[i] < 10:
                digit += nums[i]
            else:
                nums[i] = [int(i) for i in str(nums[i])]
                digit += (sum(nums[i]))
        return abs(element-digit)

# 1979. Find Greatest Common Divisor of Array
class Solution:
    def findGCD(self, nums) -> int:
        smallest = min(nums)
        largest = max(nums)
        for i in range(largest,0,-1):
            if largest % i == 0 and smallest % i == 0:
                return i

class Solution:
    def findGCD(self, nums) -> int:
        smallest = 10000
        largest = 0
        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]
            if nums[i] < smallest:
                smallest = nums[i]
        for i in range(largest,0,-1):
            if largest % i == 0 and smallest % i == 0:
                return i

# 561. Array Partition
class Solution:
    def arrayPairSum(self, nums) -> int:
        array = sorted(nums)
        result = 0
        for i in range(0,len(array),2):
            result += array[i]
        return result

# 1941. Check if All Characters Have Equal Number of Occurrences
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        results = []
        for i in range(len(s)):
            results.append(s.count(s[i]))
        print(results)
        return len(set(results)) == 1

# 1748. Sum of Unique Elements
class Solution:
    def sumOfUnique(self, nums) -> int:
        results = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1:
                i += 1
            else:
                results += nums[i]
        return results

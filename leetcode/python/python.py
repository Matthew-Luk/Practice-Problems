from typing import List, Optional, ListNode, Node
from collections import defaultdict
from heapq import heapify, heappush, heappop
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

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = [nums[0]]
        for i in nums[1:]:
            answer.append(i + answer[-1])
        return answer

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = [nums[0]]
        for i in nums[1:]:
            answer.append(i + answer[-1])
        return answer

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]

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

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0
        map = {}
        for i in nums:
            if map.get(i) is None:
                map[i] = 1
            else:
                answer += map[i]
                map[i] += 1
        return answer

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

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        map = {}
        for i in stones:
            map[i] = map.get(i,0)+1
        for i in jewels:
            if map.get(i):
                answer += map[i]
        return answer

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
        return ans

# 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        x = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= x:
                candies[i] = True
            else:
                candies[i] = False
        return candies

# 1281. Subtract the Product and Sum of Digits of an Integer
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = [int(d) for d in str(n)]
        product = 1
        for i in range(len(n)):
            product *= n[i]
        return product - sum(n)

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        while n > 0:
            product *= n%10
            sum += n%10
            n = n // 10
        return product - sum

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

class Solution:
    def interpret(self, command: str) -> str:
        answer = []
        for i in range(len(command)):
            if command[i] == "(" and command[i+1] == ")":
                answer.append("o")
            elif command[i] != "(" and command[i] != ")":
                answer.append(command[i])
        return "".join(answer)

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

class Solution:
    def shuffle(self, nums, n):
        answer = []
        for i in range(n):
            answer.append(nums[i])
            answer.append(nums[i+n])
        return answer

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
        return (int(new1) + int(new2))

class Solution:
    def minimumSum(self, num: int) -> int:
        bin = []
        while num > 0:
            bin.append(num%10)
            num = num // 10
        bin = sorted(bin)
        return (bin[0] * 10) + (bin[1] * 10) + bin[2] + bin[3]

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

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = [- x for x in nums]
        heapify(heap)

        x = heappop(heap) * -1
        y = heappop(heap) * -1

        return (x-1) * (y-1)

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

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        diff = 0
        for i in range(len(nums)):
            diff += nums[i]
            if total-diff == diff-nums[i]:
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

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, v in enumerate(nums):
            check = target - v
            if map.get(check) is not None:
                return [map[check], i]
            map[v] = i

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

# 2089. Find Target Indices After Sorting Array
class Solution:
    def targetIndices(self, nums, target: int):
        array = sorted(nums)
        results = []
        for i in range(len(array)):
            if array[i] == target:
                results.append(i)
        return results

# 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        results = []
        if len(word1) >= len(word2):
            for i in range(len(word2)):
                results.append(word1[i])
                results.append(word2[i])
            results.append(word1[len(word2):])
        elif len(word2) > len(word1):
            for i in range(len(word1)):
                results.append(word1[i])
                results.append(word2[i])
            results.append(word2[len(word1):])
        return("".join(results))

# 1720. Decode XORed Array
class Solution:
    def decode(self, encoded, first: int):
        result = [first] * (len(encoded)+1)
        for i in range(len(encoded)):
            result[i+1] = encoded[i] ^ result[i]
        return result

# 2500. Delete Greatest Value in Each Row
class Solution:
    def deleteGreatestValue(self, grid) -> int:
        rows, cols = len(grid), len(grid[0])
        result = 0
        for i in range(rows):
            grid[i] = sorted(grid[i])[::-1]
        for j in range(cols):
            temp = []
            for i in range(rows):
                temp.append(grid[i][j])
            result += max(temp)
        return result

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        answer = 0
        for i in range(len(grid)):
            grid[i] = [-x for x in grid[i]]
            heapify(grid[i])

        while grid[0]:
            temp = []
            for i in range(len(grid)):
                temp.append(heappop(grid[i])*-1)
            answer += max(temp)

        return answer

# 2574. Left and Right Sum Differences
class Solution:
    def leftRigthDifference(self, nums):
        answer = []
        for i in range(len(nums)):
            right = sum(nums[i+1:])
            left = sum(nums[:i])
            answer.append(abs(left - right))
        return answer

# 2367. Number of Arithmetic Triplets
class Solution:
    def arithmeticTriplets(self, nums, diff):
        answer = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        answer.append([i,j,k])
        return len(answer)

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        answer = 0
        map = {}
        for i, v in enumerate(nums):
            check1 = v - diff
            check2 = check1 - diff
            map[v] = i
            if map.get(check1) is not None and map.get(check2) is not None:
                answer += 1
        return answer

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        answer = 0
        seen = set()
        for i, v in enumerate(nums):
            check1 = v - diff
            check2 = check1 - diff
            seen.add(v)
            if check1 in seen and check2 in seen:
                answer += 1
        return answer

# 2485. Find the Pivot Integer
class Solution:
    def pivotInteger(self, n):
        newList = list(range(1,n+1))
        for i in range(len(newList)):
            if sum(newList[:i+1]) == sum(newList[i:]):
                return newList[i]
        return -1

class Solution:
    def pivotInteger(self, n: int) -> int:
        prefix = [0]
        for i in range(1,n+1):
            prefix.append(prefix[-1] + i)
        for i in range(1,len(prefix)):
            if prefix[-1] - prefix[i] == prefix[i-1]:
                return i
        return -1

# 2418. Sort the People
class Solution:
    def sortPeople(self, names, heights):
        answer = []
        newheights = sorted(heights,reverse = True)
        for i in range(len(newheights)):
            newheights[i] = heights.index(newheights[i])
            answer.append(names[newheights[i]])
        return answer

# 1603. Design Parking System
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big != 0:
            self.big -= 1
            return True
        elif carType == 2 and self.medium != 0:
            self.medium -= 1
            return True
        elif carType == 3 and self.small != 0:
            self.small -= 1
            return True
        return False

# 876. Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        result = []
        runner = head
        while runner != None:
            result.append(runner)
            runner = runner.next
        return result[(len(result)//2)]


# 1290. Convert Binary Number in a Linked List to Integer
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head) -> int:
        runner = head
        result = []
        while runner != None:
            result.append(str(runner.val))
            runner = runner.next
        temp = "".join(result)
        return int(temp, 2)

class Solution:
    def getDecimalValue(self, head) -> int:
        runner = head
        result = []
        while runner != None:
            result.append(runner.val)
            runner = runner.next
        # how to convert bits to integer count right to left
        # 1*2**0 + 0*2**1 + 1*2**2
        result.reverse()
        for i in range(len(result)):
            result[i] = result[i] * 2 ** i
        return sum(result)

# 412. Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int):
        result = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

# 104. Maximum Depth of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        runner = head
        while runner != None:
            next = runner.next
            runner.next = prev
            prev = runner
            runner = next
        head = prev
        return head

# 19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        length = 0
        runner = head
        while runner != None:
            length += 1
            runner = runner.next
        if length == n:
            head = head.next
        else:
            runner = head
            index = 0
            length = length - n
            while index < length - 1:
                index += 1
                runner = runner.next
            runner.next = runner.next.next
        return head

# 2652. Sum Multiples
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        answer = []
        for i in range(1,n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                answer.append(i)
        return sum(answer)

# 2656. Maximum Sum With Exactly K Elements
class Solution:
    def maximizeSum(self, nums, k) -> int:
        answer = []
        x = max(nums)
        for i in range(k):
            if i != 0:
                x += 1
            answer.append(x)
        return sum(answer)

class Solution:
    def maximizeSum(self, nums, k) -> int:
        if k == 0:
            return 0
        else:
            k -= 1
            return max(nums) + self.maximizeSum(nums, k) + k

# 2651. Calculate Delayed Arrival Time
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24

# 938. Range Sum of BST
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        if root == None:
            return 0
        if low <= root.val <= high:
            temp = root.val
        else:
            temp = 0
        return temp + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        arr = []
        def traversal(root):
            if root is None:
                return
            if low <= root.val <= high:
                arr.append(root.val)
            traversal(root.left)
            traversal(root.right)
        
        traversal(root)
        return sum(arr)

# 700. Search in a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val):
        if root == None:
            return None
        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        return self.searchBST(root.right, val)

# 2215. Find the Difference of Two Arrays
class Solution:
    def findDifference(self, nums1, nums2):
        answer = []
        temp = []
        set1 = set()
        for i in nums1:
            if i not in nums2 and i not in set1:
                    temp.append(i)
            set1.add(i)
        answer.append(temp)
        temp = []
        for i in nums2:
            if i not in nums1 and i not in set1:
                temp.append(i)
            set1.add(i)
        answer.append(temp)
        return answer

# 83. Remove Duplicates from Sorted List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return head
        duplicates = {head.val}
        slow = head
        fast = head.next
        while fast != None:
            if fast.val not in duplicates:
                duplicates.add(fast.val)
                slow = slow.next
            else:
                slow.next = fast.next
            fast = fast.next
        return head

# 2678. Number of Senior Citizens
class Solution:
    def countSeniors(self, details):
        answer = 0
        for i in range(len(details)):
            if int(details[i][11:13]) > 60:
                answer += 1
        return answer

# 2553. Separate the Digits in an Array
class Solution:
    def separateDigits(self, nums):
        answer = []
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                answer.append(int(nums[i][j]))
        return answer

# 1704. Determine if String Halves Are Alike
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        set1 = set(["a","e","i","o","u","A","E","I","O","U"])
        a, b = s[:len(s)//2], s[len(s)//2:]
        count = 0
        for i in range(len(a)):
            if a[i] in set1:
                count += 1
            if b[i] in set1:
                count -= 1
        return count == 0

# 2586. Count the Number of Vowel Strings in Range
class Solution:
    def vowelStrings(self, words, left, right):
        answer = 0
        set1 = set(["a","e","i","o","u","A","E","I","O","U"])
        for i in range(left, right+1):
            if words[i][0] in set1 and words[i][-1] in set1:
                answer += 1
        return answer

# 2278. Percentage of Letter in String
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] == letter:
                count += 1
        if count == 0:
            return count
        return math.floor(count / len(s) * 100)

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] == letter:
                count += 1
        if count == 0:
            return count
        return int(count / len(s) * 100)

# 2169. Count Operations to Obtain Zero
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        answer = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 = num1 - num2
                answer += 1
            else:
                num2 = num2 - num1
                answer += 1
        return answer

# 1880. Check if Word Equals Summation of Two Words
class Solution:
    def helper(self, word):
        answer = []
        for i in range(len(word)):
            answer.append(str(ord(word[i])-97))
        return(int("".join(answer)))

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first = self.helper(firstWord)
        second = self.helper(secondWord)
        target = self.helper(targetWord)
        return first + second == target

# 2053. Kth Distinct String in an Array
class Solution:
    def kthDistinct(self, arr, k: int) -> str:
        count = 0
        for i in range(len(arr)):
            if arr.count(arr[i]) == 1:
                count += 1
            if count == k:
                return arr[i]
        return ""

# 2496. Maximum Value of a String in an Array
class Solution:
    def maximumValue(self, strs) -> int:
        for i in range(len(strs)):
            try:
                strs[i] = int(strs[i])
            except:
                strs[i] = len(strs[i])
        return max(strs)

# 2057. Smallest Index With Equal Value
class Solution:
    def smallestEqual(self, nums) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1

# 2206. Divide Array Into Equal Pairs
class Solution:
    def divideArray(self, nums) -> bool:
        for i in range(len(nums)):
            if nums.count(nums[i]) % 2 != 0:
                return False
        return True

# 2032. Two Out of Three
class Solution:
    def twoOutOfThree(self, nums1, nums2, nums3):
        answer = []
        for i in range(len(nums1)):
            if nums2.count(nums1[i]) >= 1 or nums3.count(nums1[i]) >= 1 and nums1[i] not in answer:
                answer.append(nums1[i])
        for i in range(len(nums2)):
            if nums1.count(nums2[i]) >= 1 or nums3.count(nums2[i]) >= 1 and nums2[i] not in answer:
                answer.append(nums2[i])
        for i in range(len(nums3)):
            if nums1.count(nums3[i]) >= 1 or nums2.count(nums3[i]) >= 1 and nums3[i] not in answer:
                answer.append(nums3[i])
        return set(answer)

# 2119. A Number After a Double Reversal
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed1 = str(num)
        reversed1 = int(reversed1[::-1])
        reversed2 = str(reversed1)
        reversed2 = int(reversed2[::-1])
        return reversed2 == num

# 509. Fibonacci Number
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)

# 338. Counting Bits
class Solution:
    def countBits(self, n: int):
        answer = []
        for i in range(n+1):
            answer.append(bin(i)[2:].count("1"))
        return answer

class Solution:
    def countBits(self, n: int) -> List[int]:
        answer = []
        for i in range(n+1):
            temp = 0
            while i > 0:
                if i % 2 == 1:
                    temp += 1
                i = i // 2
            answer.append(temp)
        return answer

# 1051. Height Checker
class Solution:
    def heightChecker(self, heights) -> int:
        expected = sorted(heights)
        answer = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                answer += 1
        return answer

# 1450. Number of Students Doing Homework at a Given Time
class Solution:
    def busyStudent(self, startTime, endTime, queryTime: int) -> int:
        answer = 0
        for i in range(len(endTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                answer += 1
        return answer

# 1351. Count Negative Numbers in a Sorted Matrix
class Solution:
    def countNegatives(self, grid) -> int:
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] < 0:
                    answer += 1
        return answer

# 1935. Maximum Number of Words You Can Type
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        answer = []
        brokenLetters = set(brokenLetters)
        text = text.split(" ")
        for i in range(len(text)):
            for j in text[i]:
                if j in brokenLetters:
                    answer.append(1)
                    break
        return len(text) - len(answer)

# 2124. Check if All A's Appears Before All B's
class Solution:
    def checkString(self, s: str) -> bool:
        seen = False
        for i in range(len(s)):
            if s[i] == "b":
                seen = True
            if s[i] == "a" and seen == True:
                return False
        return True

# 1791. Find Center of Star Graph
class Solution:
    def findCenter(self, edges) -> int:
        for i in range(len(edges)):
            if edges[i][0] in edges[i+1]:
                return edges[i][0]
            elif edges[i][1] in edges[i+1]:
                return edges[i][1]

# 1374. Generate a String With Characters That Have Odd Counts
class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 0:
            return ("a"*(n-1)) + "b"
        return "a"*n

# 2325. Decode the Message
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict1 = {}
        count = 0
        key = key.replace(" ", "")
        answer = []
        for i in range(len(key)):
            if key[i] not in dict1:
                count += 1
                dict1[key[i]] = count + 96
        for i in range(len(message)):
            if message[i] != " ":
                answer.append(chr(dict1[message[i]]))
            else:
                answer.append(" ")
        return "".join(answer)

# 804. Unique Morse Code Words
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        key = {}
        temp = [".-","-...","-.-.","-..",".","..-.","--.","....",
            "..",".---","-.-",".-..","--","-.","---",".--.","--.-",
            ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        answer = []
        for i in range(len(temp)):
            key[chr(i+97)] = temp[i]
        for i in range(len(words)):
            temp = []
            for j in range(len(words[i])):
                temp.append(key[words[i][j]])
            answer.append("".join(temp))
        return len(set(answer))

# 2351. First Letter to Appear Twice
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        answer = {}
        for i in range(len(s)):
            answer[s[i]] = answer.get(s[i], 0) + 1
            if answer[s[i]] == 2:
                return s[i]

# 1486. XOR Operation in an Array
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        answer = 0
        for i in range(n):
            nums.append(start + 2 * i)
        for i in range(len(nums)):
            answer = answer ^ nums[i]
        return answer

# 66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join([str(x) for x in digits]))
        number = str(number + 1)
        number = [int(x) for x in number]
        return number

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        digits.append(0)
        digits[0] = 1
        return digits

# 202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        set1 = set()
        while n != 1:
            if n in set1:
                return False
            set1.add(n)
            temp = [int(x)**2 for x in str(n)]
            n = sum(temp)
        return True

class Solution:
    def isHappy(self, n: int) -> bool:
        set1 = set()
        while n != 1:
            if n in set1:
                return False
            set1.add(n)
            n = sum([int(x)**2 for x in str(n)])
        return True

# 1046. Last Stone Weight
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 0:
            stones = sorted(stones)
            if len(stones) == 1:
                return stones[0]
            if stones[-1] == stones[-2]:
                stones = stones[:-2]
            else:
                stones[-2] = stones[-1] - stones[-2]
                stones = stones[:-1]
        return 0

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 0:
            stones = sorted(stones)
            if len(stones) == 1:
                return stones[0]
            if stones[-1] == stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones[-2] = stones[-1] - stones[-2]
                stones.pop()
        return 0

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapify(stones)

        while len(stones) > 1:
            y = heappop(stones) * - 1
            x = heappop(stones) * - 1
            if x != y:
                stones.append(abs(y - x) * -1)

        if len(stones) == 0:
            return 0
        return stones[0] * -1

# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        answerS = {}
        answerT = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            answerS[s[i]] = answerS.get(s[i], 0) + 1
            answerT[t[i]] = answerT.get(t[i], 0) + 1
        return answerS == answerT

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s.count(s[i]) != t.count(s[i]):
                return False
        return True

# 94. Binary Tree Inorder Traversal
# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.answer=[]
        self.traversal(root)
        return self.answer
        
    def traversal(self, root):
        if root == None:
            return
        self.traversal(root.left)
        self.answer.append(root.val)
        self.traversal(root.right)

# 144. Binary Tree Preorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        self.traversal(root)
        return self.answer

    def traversal(self, root):
        if root == None:
            return
        self.answer.append(root.val)
        self.traversal(root.left)
        self.traversal(root.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        while root or stack:
            while root:
                stack.append(root)
                result.append(root.val)
                root = root.left

            root = stack.pop()
            root = root.right
        return result

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

# 1299. Replace Elements with Greatest Element on Right Side
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        while s[-1] == " ":
            s = s[:-1]
        s = s.split(" ")
        count = 0
        for i in s[-1]:
            count += 1
        return count

# 27. Remove Element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]
        return len(nums)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i

# 169. Majority Element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = {}
        for i in range(len(nums)):
            answer[nums[i]] = answer.get(nums[i], 0) + 1
        return max(answer, key=answer.get)

# 448. Find All Numbers Disappeared in an Array
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        temp = set(list(nums))
        for i in range(1,len(nums)+1):
            if i not in temp:
                answer.append(i)
        return answer

# 1299. Replace Elements with Greatest Element on Right Side
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        temp = arr[-1]
        for i in range(len(arr)-1,-1,-1):
            if arr[i] > temp:
                temp = arr[i]
            arr[i] = temp
        arr.append(-1)
        arr.pop(0)
        return arr

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        answer, stack = [], []
        for i in range(len(arr)-1,-1,-1):
            if answer == []:
                answer.append(-1)
                stack.append(arr[i])
            else:
                if arr[i] > stack[-1]:
                    answer.append(stack[-1])
                    stack.append(arr[i])
                else:
                    answer.append(stack[-1])
        return answer[::-1]

# 290. Word Pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        answer = {}
        words = s.split(" ")
        if len(set(words)) != len(set(pattern)) or len(words) != len(pattern):
            return False
        for i in range(len(words)):
            if words[i] not in answer:
                answer[words[i]] = pattern[i]
            else:
                if answer[words[i]] != pattern[i]:
                    return False
        return True

# 496. Next Greater Element I
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums1)):
            seen = False
            for j in range(len(nums2)):
                if seen == True:
                    if nums2[j] > nums1[i]:
                        answer.append(nums2[j])
                        break
                elif seen == False and nums1[i] == nums2[j]:
                    seen = True
            if len(answer) != i+1:
                answer.append(-1)
        return answer

# 1523. Count Odd Numbers in an Interval Range
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 1 or high % 2 == 1:
            return ((high-low) // 2) + 1
        return ((high-low) // 2)

# 1572. Matrix Diagonal Sum
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        arr = []
        result = 0
        for i in range(len(mat)):
            arr.append([i,i])
            if [len(mat)-1-i,i] not in arr:
                arr.append([len(mat)-1-i,i])
        for i in arr:
            result += mat[i[0]][i[1]]
        return 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack.count(needle) == 0:
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                x = 0
                for j in range(len(needle)):
                    if needle[j] == haystack[i+j]:
                        x += 1
                    if x == len(needle):
                        return i
        return -1

# 28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                x = 0
                for j in range(len(needle)):
                    try:
                        if haystack[i+j] == needle[j]:
                            x += 1
                        if x == len(needle):
                            return i
                    except:
                        return -1
        return -1

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                if haystack[i:i+len(needle)] == needle:
                    return i

# 1822. Sign of the Product of an Array
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for i in nums:
            product *= i
        return 1 if product > 0 else (-1 if product < 0 else 0)

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        negative = 0
        for i in nums:
            if i == 0:
                return 0
            elif i < 0:
                negative += 1
        if negative % 2 == 0:
            return 1
        return -1

# 1189. Maximum Number of Balloons
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map = {"b":0,"a":0,"l":0,"o":0,"n":0}
        for i in range(len(text)):
            if text[i] in map:
                if text[i] == "l" or text[i] == "o":
                    map[text[i]] += 0.5
                else:
                    map[text[i]] += 1
        min = map["b"]
        for key in map:
            if map[key] < min:
                min = map[key]
        return int(min)

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        map = {}
        for i in range(len(text)):
            if text[i] in "balon":
                if text[i] == "l" or text[i] == "o":
                    map[text[i]] = map.get(text[i], 0) + 0.5
                else:
                    map[text[i]] = map.get(text[i], 0) + 1
        if len(map) < 5:
            return 0
        else:
            min = list(map.values())[0]
            for key in map:
                if map[key] < min:
                    min = map[key]
            return int(min)

# 303. Range Sum Query - Immutable
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        
    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])

# 205. Isomorphic Strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map = {}
        if len(set(s)) != len(set(t)):
            return False
        for i in range(len(s)):
            if map.get(s[i]) == None:
                map[s[i]] = t[i]
            else:
                if map.get(s[i]) != t[i]:
                    return False
        return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        key = {}
        for i in range(len(s)):
            key[s[i]] = t[i]
        if len(key.values()) != len(set(key.values())):
            return False
        answer = []
        for i in s:
            if key.get(i) is None:
                return False
            answer.append(key[i])
        return "".join(answer) == t

# 705. Design HashSet
class MyHashSet:
    def __init__(self):
        self.hash_set = set()
        
    def add(self, key: int) -> None:
        self.hash_set.add(key)
        
    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hash_set.remove(key)
        
    def contains(self, key: int) -> bool:
        return key in self.hash_set

# 929. Unique Email Addresses
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            emails[i] = emails[i].split("@")
            emails[i][0] = emails[i][0].replace(".","")
            emails[i] = "@".join(emails[i])
            if emails[i].count("+") > 0:
                emails[i] = emails[i][:emails[i].index("+")] + emails[i][emails[i].index("@"):]
        return len(set(emails))

# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reverse = [i for i in str(x)[::-1]]
        return int("".join(reverse)) == x

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        bin = []
        while x > 0:
            bin.append(x%10)
            x = x // 10
        l = 0
        r = len(bin) -1
        while l < r:
            if bin[l] != bin[r]:
                return False
            l += 1
            r -= 1
        return True

# 234. Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        runner = head
        while runner != None:
            arr.append(runner.val)
            runner = runner.next
        reverse = arr[::-1]
        return arr == reverse

# 125. Valid Palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [x for x in s if ord(x) >= 97 and ord(x) <= 122 or ord(x) >= 48 and ord(x) <= 57]
        l = 0
        r = len(s) -1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [x for x in s if ord(x) >= 97 and ord(x) <= 122 or ord(x) >= 48 and ord(x) <= 57]
        return s == s[::-1]

# 145. Binary Tree Postorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.answer = []
        self.traversal(root)
        return self.answer

    def traversal(self, root):
        if root == None:
            return
        self.traversal(root.left)
        self.traversal(root.right)
        self.answer.append(root.val)

# 110. Balanced Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root == None:
            return - 1
        else:
            return 1 + max(self.height(root.left), self.height(root.right))

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if abs(lh - rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

# 783. Minimum Distance Between BST Nodes
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        arr = []
        def traversal(root):
            if root == None:
                return
            traversal(root.left)
            arr.append(root.val)
            traversal(root.right)
        traversal(root)
        
        min = arr[-1]
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] < min:
                min = arr[i+1] - arr[i]
        return min

# 225. Implement Stack using Queues
from collections import deque
class MyStack:

    def __init__(self):
        self.queue = deque()
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        
    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            self.push(self.queue.popleft())
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[-1]
        
    def empty(self) -> bool:
        return len(self.queue) == 0
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == ")" and len(stack) == 0 or i == "]" and len(stack) == 0 or i == "}" and len(stack) == 0:
                return False
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif i == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif i == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif i == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            elif stack == []:
                return False
            elif i == ")" and stack[-1] == "(" or i == "]" and stack[-1] == "[" or i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        return len(stack) == 0

# 682. Baseball Game
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "C":
                stack.pop()
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(i))
        return sum(stack)

# 155. Min Stack
# LIFO
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if self.stack == []:
            self.stack.append(val)
            self.minstack.append(val)
        else:
            if val < self.minstack[-1]:
                self.stack.append(val)
                self.minstack.append(val)
            else:
                self.stack.append(val)
                self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# 2390. Removing Stars From a String
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)

# 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        answer = 0
        for i in t:
            if answer == len(s):
                return True
            elif s[answer] == i:
                answer += 1
        return answer == len(s)

# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        temp = min([len(x) for x in strs])
        count = 0
        while count < temp:
            x = strs[0][count]
            y = 0
            for i in range(len(strs)):
                if strs[i][count] == x:
                    y += 1
                if strs[i][count] != x:
                    return answer
                elif y == len(strs):
                    answer += x
            count += 1
        return answer

# 706. Design HashMap
class MyHashMap:

    def __init__(self):
        self.map = [None for _ in range(1000001)]
        
    def put(self, key: int, value: int) -> None:
        self.map[key] = value
        
    def get(self, key: int) -> int:
        if self.map[key] != None:
            return self.map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if self.map[key]:
            self.map[key] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l < r:
            temp = numbers[l] + numbers[r]
            if temp == target:
                return [l+1, r+1]
            elif temp < target:
                l += 1
            else:
                r -= 1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while numbers[l] + numbers[r] != target:
            temp = numbers[l] + numbers[r]
            if temp < target:
                l += 1
            else:
                r -= 1
        return [l+1, r+1]

# 263. Ugly Number
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n = n // 2
        while n % 3 == 0:
            n = n // 3
        while n % 5 == 0:
            n = n // 5
        return n == 1

# 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        answer = 0
        key = {"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}

        for i in range(len(s)-1):
            if key[s[i]] < key[s[i+1]]:
                answer -= key[s[i]]
            else:
                answer += key[s[i]]
        answer += key[s[-1]]
        return answer

# 12. Integer to Roman
class Solution:
    def intToRoman(self, num: int) -> str:
        answer = ""
        roman = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40,"X":10, "IX":9, "V":5, "IV": 4, "I": 1}

        for key in roman:
            while num // roman[key] >= 1:
                answer += key
                num -= roman[key]
        return answer

# 50. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x ** n

# 43. Multiply Strings
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        answer = eval(num1+"*"+num2)
        return (str(answer))

# 49. Group Anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        answer = []

        for i in range(len(strs)):
            temp = "".join(sorted(strs[i]))
            if map.get(temp) == None:
                map[temp] = [strs[i]]
            else:
                map[temp].append(strs[i])

        for key in map:
            answer.append(map[key])

        return answer

# 1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))

# 2396. Strictly Palindromic Number
class Solution:
    def numberToBase(self, n, b):
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]

    def isPalindrome(self, arr):
        l = 0
        r = len(arr) -1
        while l <= r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True

    def isStrictlyPalindromic(self, n: int) -> bool:
        temp = []
        for i in range(2,n+1):
            if self.isPalindrome(self.numberToBase(n,i)) == False:
                return False
        return True

# 2697. Lexicographically Smallest Palindrome
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l = 0
        r = len(s) -1
        s = [x for x in s]
        while l <= r:
            if s[l] != s[r]:
                if ord(s[l]) < ord(s[r]):
                    s[r] = s[l]
                else:
                    s[l] = s[r]
            l += 1
            r -= 1
        return "".join(s)

# 2220. Minimum Bit Flips to Convert Number
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        startbit = bin(start)[:1:-1]
        goalbit = bin(goal)[:1:-1]
    
        if len(startbit) <= len(goalbit):
            shorter, longer = startbit, goalbit
        else:
            shorter, longer = goalbit, startbit

        while len(shorter) != len(longer):
            shorter += "0"

        answer = 0
        for i in range(len(shorter)):
            if shorter[i] != longer[i]:
                answer += 1
        return answer

# 1614. Maximum Nesting Depth of the Parentheses
class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        max = 0
        for i in s:
            if i == "(":
                count += 1
            if count > max:
                max = count
            elif i == ")":
                count -= 1
        return max

# 2733. Neither Minimum nor Maximum
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1
        else:
            nums = sorted(nums)
            return nums[len(nums)//2]

# 2710. Remove Trailing Zeros From a String
class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        while num[-1] == "0":
            num = num[:-1]
        return num

# 1827. Minimum Operations to Make the Array Increasing
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        answer = 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                answer += nums[i-1] + 1 - nums[i]
                nums[i] = nums[i-1] + 1
        return answer

# 2108. Find First Palindromic String in the Array
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            l = 0
            r = len(word) -1
            count = 0
            while l <= r:
                if l == r:
                    count += 1
                elif word[l] == word[r]:
                    count += 2
                l += 1
                r -= 1
            if count == len(word):
                return word 
        return ""

# 1812. Determine Color of a Chessboard Square
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0])-97
        if x % 2 == 0:
            return int(coordinates[1]) % 2 == 0
        return int(coordinates[1]) % 2 == 1

# 1725. Number Of Rectangles That Can Form The Largest Square
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        answer = []
        for i in rectangles:
            answer.append(min(i))
        return answer.count(max(answer))

# 2670. Find the Distinct Difference Array
class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            answer.append(len(set(nums[:i+1])) - len(set(nums[i+1:])))
        return answer

# 461. Hamming Distance
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]
        
        if len(x) < len(y):
            shorter, longer = x, y
        else:
            shorter, longer = y, x

        while len(shorter) != len(longer):
            shorter = "0" + shorter

        answer = 0
        for i in range(len(shorter)):
            if shorter[i] != longer[i]:
                answer += 1
        return answer

# 657. Robot Return to Origin
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        answer = [0,0]
        for i in moves:
            if i == "U":
                answer[0] += 1
            elif i == "D":
                answer[0] -= 1
            elif i == "L":
                answer[1] += 1
            else:
                answer[1] -= 1
        return answer == [0,0]

# 1475. Final Prices With a Special Discount in a Shop
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] = prices[i] - prices[j]
                    break
        return prices

# 1207. Unique Number of Occurrences
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        map = {}
        answer = []
        for i in arr:
            map[i] = map.get(i, 0) + 1
        for value in map.values():
            answer.append(value)
        return len(answer) == len(set(answer))

# 2716. Minimize String Length
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))

class Solution:
    def minimizedStringLength(self, s: str) -> int:
        set1 = set()
        for i in s:
            if i not in set1:
                set1.add(i)
        answer = 0
        for i in set1:
            answer += 1
        return answer

# 2529. Maximum Count of Positive Integer and Negative Integer
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive = 0
        negative = 0
        for i in nums:
            if i < 0:
                negative += 1
            elif i > 0:
                positive += 1
        return max(positive, negative)

# 2154. Keep Multiplying Found Values by Two
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2
        return original

# 2255. Count Prefixes of a Given String
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        answer = 0
        for i in words:
            if i == s[:len(i)]:
                answer += 1
        return answer

# 136. Single Number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

# 2578. Split With Minimum Sum
class Solution:
    def splitNum(self, num: int) -> int:
        num = sorted([x for x in str(num)])
        num1, num2 = [], []
        for i in range(len(num)):
            if i % 2 == 0:
                num1.append(num[i])
            else:
                num2.append(num[i])
        num1 = int("".join(num1))
        num2 = int("".join(num2))
        return num1 + num2

# 1436. Destination City
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        map = {}
        for i in paths:
            map[i[0]] = i[1]
        cities = map.keys()
        for value in map.values():
            if value not in cities:
                return value

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        map = {}
        for i in paths:
            map[i[0]] = i[1]
        for value in map.values():
            if value not in map.keys():
                return value

# 2595. Number of Even and Odd Bits
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        answer = [0,0]
        n = bin(n)[:1:-1]
        for i in range(len(n)):
            if n[i] == "1":
                if i % 2 == 0:
                    answer[0] += 1
                else:
                    answer[1] += 1
        return answer

# 922. Sort Array By Parity II
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        answer = []
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(even)):
            answer.append(even[i])
            answer.append(odd[i])
        return answer

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        even = 0
        odd = 1
        for i in nums:
            if i % 2 == 0:
                answer[even] = i
                even += 2
            else:
                answer[odd] = i
                odd += 2
        return answer

# 905. Sort Array By Parity
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        even = 0
        odd = len(nums) -1
        for i in nums:
            if i % 2 == 0:
                answer[even] = i
                even += 1
            else:
                answer[odd] = i
                odd -= 1
        return answer

# 2283. Check if Number Has Equal Digit Count and Digit Value
class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if str(num.count(str(i))) != num[i]:
                return False
        return True

class Solution:
    def digitCount(self, num: str) -> bool:
        for i in range(len(num)):
            if num.count(str(i)) != int(num[i]):
                return False
        return True

# 1991. Find the Middle Index in Array
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count == sum(nums[i:]):
                return i
        return -1

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        left = [sum(nums[:i]) for i in range(len(nums))]
        right = [sum(nums[i+1:]) for i in range(len(nums))]
        for i in range(len(left)):
            if left[i] == right[i]:
                return i
        return -1

# 2506. Count Pairs Of Similar Strings
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        answer = 0
        for i in range(len(words)):
            temp_set = set(words[i])
            for j in range(i+1,len(words)):
                temp_set2 = set(words[j])
                if temp_set == temp_set2:
                    answer += 1
        return answer

# 2085. Count Common Words With One Occurrence
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        answer = 0
        for i in words1:
            if words1.count(i) == 1 and words2.count(i) == 1:
                answer += 1
        return answer

# 2562. Find the Array Concatenation Value
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        answer = 0
        while len(nums) > 0:
            if len(nums) == 1:
                answer += nums[0]
                break
            temp = str(nums[0]) + str(nums[-1])
            answer += int(temp)
            nums = nums[1:-1]
        return answer

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        answer = 0
        l = 0
        r = len(nums) -1
        while l <= r:
            if l == r:
                answer += nums[r]
                break
            temp = str(nums[l]) + str(nums[r])
            answer += int(temp)
            l += 1
            r -= 1
        return answer

# 500. Keyboard Row
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        alphabet = {"q":1,"w":1,"e":1,"r":1,"t":1,"y":1,"u":1,"i":1,"o":1,"p":1, 
                    "a":2,"s":2,"d":2,"f":2,"g":2,"h":2,"j":2,"k":2,"l":2,
                    "z":3,"x":3,"c":3,"v":3,"b":3,"n":3,"m":3}

        answer = []
        for i in range(len(words)):
            lower = words[i].lower()
            temp = []
            for j in lower:
                temp.append(alphabet[j])
            if len(set(temp)) == 1:
                answer.append(words[i])
        return answer

# 2309. Greatest English Letter in Upper and Lower Case
class Solution:
    def greatestLetter(self, s: str) -> str:
        answer = []
        for i in s:
            answer.append(ord(i))
        answer = sorted(answer, reverse=True)
        for i in answer:
            search = i - 32
            if search in answer:
                return chr(i - 32)
        return ""

class Solution:
    def greatestLetter(self, s: str) -> str:
        letters = set(s)
        letters = sorted(letters, reverse=True)
        for i in letters:
            if i.lower() in letters and i.upper() in letters:
                return i.upper()
        return ""

# 2544. Alternating Digit Sum
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num = [int(x) for x in str(n)]
        answer = 0
        for i in range(len(num)):
            if i % 2 == 0:
                answer += num[i]
            else:
                answer -= num[i]
        return answer

# 728. Self Dividing Numbers
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        results = []
        for i in range(left,right+1):
            count = 0
            if str(i).count("0"):
                continue
            for j in str(i):
                if i % int(j) == 0:
                    count += 1
                if count == len(str(i)):
                    results.append(i)
        return results

# 2103. Rings and Rods
class Solution:
    def countPoints(self, rings: str) -> int:
        map = {}
        for i in range(0,len(rings),2):
            if map.get(rings[i+1]) == None:
                map[rings[i+1]] = [rings[i]]
            else:
                map[rings[i+1]].append(rings[i])

        answer = 0
        for value in map.values():
            if len(set(value)) == 3:
                answer += 1
        return answer

# 1502. Can Make Arithmetic Progression From Sequence
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        temp = sorted(arr)
        progression = abs(temp[0] - temp[1])
        for i in range(len(temp)-1):
            if abs(temp[i] - temp[i+1]) != progression:
                return False
        return True

# 944. Delete Columns to Make Sorted
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        answer = 0
        i = 0
        while i < len(strs[0]):
            temp = []
            for j in range(len(strs)):
                if j != 0 and ord(strs[j][i]) < temp[-1]:
                    answer += 1
                    break
                temp.append(ord(strs[j][i]))
            i += 1
        return answer

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        answer = 0
        i = 0
        while i < len(strs[0]):
            temp = []
            for j in range(len(strs)):
                temp.append(ord(strs[j][i]))
            if temp != sorted(temp):
                answer += 1
            i += 1
        return answer

# 2643. Row With Maximum Ones
class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        answer = [0,0]
        for i in range(len(mat)):
            count = 0
            for j in mat[i]:
                if j == 1:
                    count += 1
            mat[i] = count
            if count > answer[1]:
                answer = [i,count]
        return answer

# 21. Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current = head

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1 or list2:
            current.next = list1 if list1 else list2
        
        return head.next

# 1974. Minimum Time to Type Word Using Special Typewriter
class Solution:
    def minTimeToType(self, word: str) -> int:
        answer = 0
        order = []
        for i in range(len(word)):
            order.append(ord(word[i]) - 97)
        for j in range(len(order)):
            if j == 0:
                answer += min(order[j], abs(26 - order[j]))
            else:
                if order[j] <= order[j-1]:
                    answer += min(abs(order[j] - order[j-1]), abs(26 - order[j-1]) + order[j])
                else:
                    answer += min(abs(order[j] - order[j-1]), abs(26 - order[j]) + order[j-1])
        return answer + len(word)

class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = len(word)
        prev = "a"
        for ch in word: 
            val = (ord(ch) - ord(prev)) % 26 
            ans += min(val, 26 - val)
            prev = ch
        return ans 

# 1460. Make Two Arrays Equal by Reversing Subarrays
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if list == arr:
            return True
        map = {}
        for i in range(len(arr)):
            map[arr[i]] = map.get(arr[i],0) + 1
            map[target[i]] = map.get(target[i],0) - 1

        for v in map.values():
            if v != 0:
                return False
        return True

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)

# 821. Shortest Distance to a Character
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        location = []
        answer = []
        for i in range(len(s)):
            if s[i] == c:
                location.append(i)
        for i in range(len(s)):
            min = len(s)
            for j in location:
                if abs(j-i) < min:
                    min = abs(j-i)
            answer.append(min)
        return answer

# 1200. Minimum Absolute Difference
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        answer = []
        min = arr[-1]
        for i in range(1,len(arr)):
            if abs(arr[i] - arr[i-1]) < min:
                min = abs(arr[i] - arr[i-1])
        for i in range(1,len(arr)):
            if abs(arr[i] - arr[i-1]) == min:
                answer.append([arr[i-1],arr[i]])
        return answer

# 2460. Apply Operations to an Array
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
        return nums

# 258. Add Digits
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = sum([int(x) for x in str(num)])
        return num

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9

# 2180. Count Integers With Even Digit Sum
class Solution:
    def countEven(self, num: int) -> int:
        answer = 0
        for i in range(1,num+1):
            temp = sum([int(x) for x in str(i)])
            if temp % 2 == 0:
                answer += 1
        return answer

# 1137. N-th Tribonacci Number
class Solution:
    def tribonacci(self, n: int) -> int:
        fib = [0,1,1]
        if n <= 2:
            return fib[n]
        else:
            for i in range(3,n):
                fib.append(fib[-1] + fib[-2] + fib[-3])
        return fib[-1] + fib[-2] + fib[-3]

# 1408. String Matching in an Array
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        answer = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j] and words[i] not in answer:
                    answer.append(words[i])
                elif words[j] in words[i] and words[j] not in answer:
                    answer.append(words[j])
        return answer

# 2068. Check Whether Two Strings are Almost Equivalent
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        map = {}
        for letter in word1:
            map[letter] = map.get(letter,0) +1
        for letter in word2:
            map[letter] = map.get(letter,0) -1
        for v in map.values():
            if v < -3 or v > 3:
                return False
        return True

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        for i in range(len(word1)):
            if abs(word1.count(word1[i]) - word2.count(word1[i])) > 3:
                return False
            elif abs(word2.count(word2[i]) - word1.count(word2[i])) > 3:
                return False
        return True

# 268. Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = list(range(0,max(nums)+1))
        if sum(arr) - sum(nums) == 0:
            if 0 not in nums:
                return 0
            else:
                return max(nums) + 1
        return sum(arr) - sum(nums)

# 1550. Three Consecutive Odds
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in arr:
            if i % 2 == 1:
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
        return False

# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original:
            return None
        else:
            if original == target:
                return cloned
            return self.getTargetCopy(original.left, cloned.left, target) or self.getTargetCopy(original.right, cloned.right, target)

# 2744. Find Maximum Number of String Pairs
class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        answer = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i][0] == words[j][1] and words[i][1] == words[j][0]:
                    answer += 1
        return answer

# 1742. Maximum Number of Balls in a Box
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        answer = 0
        for i in range(lowLimit, highLimit +1):
            temp = sum([int(x) for x in str(i)])
            boxes[temp] = boxes.get(temp,0) + 1
            if boxes[temp] > answer:
                answer = boxes[temp]
        return answer

# 2558. Take Gifts From the Richest Pile
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        answer = 0
        while k > 0:
            gifts[gifts.index(max(gifts))] = int(math.sqrt(max(gifts)))
            k -= 1
        return sum(gifts)

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            gifts = sorted(gifts)
            temp = int(math.sqrt(gifts[-1]))
            gifts[-1] = temp
            k -= 1
        return sum(gifts)

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        heapify(gifts)

        while k > 0:
            x = heappop(gifts) * -1
            x = math.sqrt(x) // 1
            heappush(gifts, x * -1)
            k -= 1

        return int(sum(gifts) * -1)

# 2441. Largest Positive Integer That Exists With Its Negative
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse=True)
        for i in range(len(nums)):
            if nums[i] * -1 in nums:
                return nums[i]
        return -1

# 824. Goat Latin
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = "aeiouAEIOU"
        sentence = sentence.split(" ")
        answer = []
        for i in range(len(sentence)):
            if sentence[i][0] in vowels:
                answer.append(sentence[i] + "ma" + ("a"*(i+1)))
            elif sentence[i][0] not in vowels:
                answer.append(sentence[i][1:] + sentence[i][0] + "ma" + ("a"*(i+1)))
        return " ".join(answer)

# 908. Smallest Range I
class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        if (max(nums)-k) - (min(nums)+k) > 0:
            return (max(nums)-k) - (min(nums)+k)
        return 0

# 2042. Check if Numbers Are Ascending in a Sentence
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = [int(x) for x in s.split() if x.isdigit()]
        for i in range(len(s)-1):
            if s[i] >= s[i+1]:
                return False
        return True

# 535. Encode and Decode TinyURL
class Codec:
    def encode(self, longUrl: str) -> str:
        return longUrl
    def decode(self, shortUrl: str) -> str:
        return shortUrl

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

# 1967. Number of Strings That Appear as Substrings in Word
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        answer = 0
        for i in patterns:
            if i in word:
                answer += 1
        return answer

# 1252. Cells with Odd Values in a Matrix
class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = []
        while m > 0:
            mat.append([0]*n)
            m -= 1
        for i in indices:
            mat[i[0]] = [x + 1 for x in mat[i[0]]]
            for j in mat:
                j[i[1]] += 1

        answer = 0
        for i in range(len(mat)):
            for j in mat[i]:
                if j % 2 != 0:
                    answer += 1
        return answer

# 1309. Decrypt String from Alphabet to Integer Mapping
class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = []
        for i in range(len(s)):
            if s[i] != "#":
                answer.append(chr(int(s[i])+96))
            else:
                temp = ((ord(answer[-2])-96) * 10) + ord(answer[-1])-96
                answer = answer[:-2]
                answer.append(chr(temp+96))
        return "".join(answer)

# 1710. Maximum Units on a Truck
class Solution:
    def Sort(self, sub_li):
        l = len(sub_li)
        for i in range(0, l):
            for j in range(0, l-i-1):
                if (sub_li[j][1] > sub_li[j + 1][1]):
                    tempo = sub_li[j]
                    sub_li[j] = sub_li[j + 1]
                    sub_li[j + 1] = tempo
        return sub_li[::-1]

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        answer = 0
        boxTypes = self.Sort(boxTypes)
        for i in range(len(boxTypes)):
            if boxTypes[i][0] < truckSize:
                answer = answer + (boxTypes[i][0] * boxTypes[i][1])
                truckSize -= boxTypes[i][0]
            else:
                for j in range(boxTypes[i][0]):
                    if truckSize == 0:
                        return answer
                    answer += boxTypes[i][1]
                    truckSize -= 1
        return answer

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        answer = 0
        boxTypes.sort(reverse=True, key=lambda x:x[1])
        for i in range(len(boxTypes)):
            if boxTypes[i][0] < truckSize:
                answer = answer + (boxTypes[i][0] * boxTypes[i][1])
                truckSize -= boxTypes[i][0]
            else:
                for j in range(boxTypes[i][0]):
                    if truckSize == 0:
                        return answer
                    answer += boxTypes[i][1]
                    truckSize -= 1
        return answer

# 942. DI String Match
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        answer = []
        newlist = list(range(len(s)+1))
        l = 0
        r = len(s)
        for i in s:
            if i == "I":
                answer.append(newlist[l])
                l += 1
            else:
                answer.append(newlist[r])
                r -= 1
        answer.append(newlist[r])
        return answer

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        answer = []
        l, r = 0, len(s)
        for i in s:
            if i == "I":
                answer.append(l)
                l += 1
            else:
                answer.append(r)
                r -= 1
        answer.append(r)
        return answer

# 2769. Find the Maximum Achievable Number
class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t + t

# 1221. Split a String in Balanced Strings
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        answer = 0
        count = 0
        for i in s:
            if i == "R":
                count += 1
            if i == "L":
                count -= 1
            if count == 0:
                answer += 1
        return answer

# 1656. Design an Ordered Stream
class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None] * n
        self.ptr = 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1
        self.stream[idKey] = value
        if self.ptr < idKey:
            return []
        else:
            while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
                self.ptr += 1
            return self.stream[idKey:self.ptr]

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

# 2373. Largest Local Values in a Matrix
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        answer = []
        for i in range(1,len(grid)-1):
            temp = []
            for j in range(1,len(grid[i])-1):
                temp.append(max(grid[i-1][j-1:j+2] + grid[i][j-1:j+2] + grid[i+1][j-1:j+2]))
            answer.append(temp)
        return answer

# 1534. Count Good Triplets
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        answer = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                for k in range(j+1,len(arr)):
                    if a >= abs(arr[i] - arr[j]) and b >= abs(arr[j] - arr[k]) and c >= abs(arr[i] - arr[k]):
                        answer += 1
        return answer

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        answer = 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if a < abs(arr[i] - arr[j]):
                    continue
                for k in range(j+1,len(arr)):
                    if b < abs(arr[j] - arr[k]):
                        continue
                    elif c >= abs(arr[i] - arr[k]):
                        answer += 1
        return answer

# 897. Increasing Order Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, root):
        if root == None:
            return
        self.traversal(root.left)
        self.list.append(root.val)
        self.traversal(root.right)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.list = []
        self.traversal(root)
        answer = TreeNode(self.list[0])
        current = answer
        i = 1
        while i < len(self.list):
            current.right = TreeNode(self.list[i])
            current = current.right
            i += 1
        return answer

# 1356. Sort Integers by The Number of 1 Bits
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        answer = []
        map = {}
        for i in range(len(arr)):
            temp = str(bin(arr[i]))
            if map.get(temp.count("1")) == None:
                map[temp.count("1")] = [arr[i]]
            else:
                map[temp.count("1")].append(arr[i])
        myKeys = list(map.keys())
        myKeys.sort()
        sorted_dict = {i: map[i] for i in myKeys}
        for i in sorted_dict.values():
            answer = answer + sorted(i)
        return answer

# 1370. Increasing Decreasing String
class Solution:
    def sortString(self, s: str) -> str:
        result = ""
        s = list(s)
        while s:
            for i in sorted(set(s)):
                s.remove(i)
                result += i
            for i in sorted(set(s), reverse=True):
                s.remove(i)
                result += i
        return result

# 1304. Find N Unique Integers Sum up to Zero
class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        if n == 1:
            return [0]
        elif n % 2 == 0:
            for i in range(1,(n//2)+1):
                answer.append(i)
                answer.append(i*-1)
            return answer
        else:
            for i in range(1,(n//2)+1):
                answer.append(i)
                answer.append(i*-1)
            answer.append(0)
            return answer

class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        for i in range(1,(n//2)+1):
            answer.append(i)
            answer.append(i*-1)
        if n % 2 == 1:
            answer.append(0)
        return answer

# 231. Power of Two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        key = []
        for i in range(32):
            key.append(2 ** i)
        return n in key

# 387. First Unique Character in a String
class Solution:
    def firstUniqChar(self, s: str) -> int:
        answer = {}
        for i in range(len(s)):
            if s.count(s[i]) == 1:
                return i
        return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        answer = {}
        for i in range(len(s)):
            answer[s[i]] = answer.get(s[i],0) + 1
        for k, v in answer.items():
            if v == 1:
                return s.index(k)
        return -1

# 389. Find the Difference
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if s.count(i) != t.count(i):
                return i

# 345. Reverse Vowels of a String
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        key = []
        for i in s:
            if i in vowels:
                key.append(i)
        index = len(key) - 1
        answer = []
        for i in s:
            if i in vowels:
                answer.append(key[index])
                index -= 1
            else:
                answer.append(i)
        return "".join(answer)

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = [x for x in s]
        l = 0
        r = len(s) -1
        while l <= r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            else:
                if s[l] not in vowels:
                    l += 1
                if s[r] not in vowels:
                    r -= 1
        return "".join(s)

# 342. Power of Four
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        key = [4 ** x for x in range(16)]
        return n in key

# 349. Intersection of Two Arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        nums1, nums2 = list(set(nums1)), list(set(nums2))
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        for i in nums1:
            if i in nums2 and i not in answer:
                answer.append(i)
        return answer

# 350. Intersection of Two Arrays II
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        for i in nums1:
            if i in nums2 and answer.count(i) < min(nums1.count(i), nums2.count(i)):
                answer.append(i)
        return answer

# 703. Kth Largest Element in a Stream
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.list = nums
        self.k = k

    def add(self, val: int) -> int:
        self.list.append(val)
        self.list = sorted(self.list)
        return self.list[-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

# 747. Largest Number At Least Twice of Others
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max = [0,0]
        for i in range(len(nums)):
            if nums[i] > max[0]:
                max[0] = nums[i]
                max[1] = i
        count = 0
        for i in nums:
            if max[0] >= i * 2:
                count += 1
        if count == len(nums)-1:
            return max[1]
        return -1

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        count = 0
        x = max(nums)
        for i in nums:
            if x == i or x >= i * 2:
                count += 1
        if count == len(nums):
            return nums.index(x)
        return -1

# 744. Find Smallest Letter Greater Than Target
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        x = [ord(x) for x in letters]
        target = ord(target)
        if target < x[0] or target >= x[-1]:
            return chr(x[0])
        for i in x:
            if i > target:
                return chr(i)

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]

# 819. Most Common Word
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        map = {}
        punctuation = "!?',;."
        for i in paragraph:
            if i in punctuation:
                paragraph = paragraph.replace(i, " ")
        paragraph = paragraph.lower()
        paragraph = paragraph.split(" ")
        paragraph = [x for x in paragraph if x != ""]
        for i in paragraph:
            if i not in banned:
                map[i] = map.get(i,0) +1
        x = max(map.values())
        for k, v in map.items():
            if v == x:
                return k

# 844. Backspace String Compare
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for i in s:
            if i != "#":
                stack1.append(i)
            else:
                if stack1:
                    stack1.pop()
        for i in t:
            if i != "#":
                stack2.append(i)
            else:
                if stack2:
                    stack2.pop()
        return "".join(stack1) == "".join(stack2)

# 917. Reverse Only Letters
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        if len(s) == 1:
            return s
        l = 0
        r = len(s) -1
        s = [x for x in s]
        while l <= r:
            if s[l] != "-" and s[r] != "-":
                if s[l].isalpha() and s[r].isalpha():
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
            if s[l] == "-" or s[l].isalpha() == False:
                l += 1
            if s[r] == "-" or s[r].isalpha() == False:
                r -= 1
        return "".join(s)

# 896. Monotonic Array
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        return nums == sorted(nums) or nums == sorted(nums, reverse=True)

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] < nums[-1]:
            for i in range(1,len(nums)):
                if nums[i-1] > nums[i]:
                    return False
            return True
        else:
            for i in range(1,len(nums)):
                if nums[i-1] < nums[i]:
                    return False
            return True

# 961. N-Repeated Element in Size 2N Array
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        map = {}
        for i in nums:
            map[i] = map.get(i,0) + 1
            if map[i] == 2:
                return i

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        list = []
        for i in nums:
            if i in list:
                return i
            if i not in list:
                list.append(i)

# 1154. Day of the Year
class Solution:
    def isLeapYear(self, year):
        year = int(year)
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
            return True

    def dayOfYear(self, date: str) -> int:
        month = {
            "01": 0,
            "02": 31,
            "03": 59,
            "04": 90,
            "05": 120,
            "06": 151,
            "07": 181,
            "08": 212,
            "09": 243,
            "10": 273,
            "11": 304,
            "12": 334,
        }

        answer = month[date[5:7]] + int(date[8:10])
        if self.isLeapYear(date[0:4]) and int(date[5:7]) > 2:
            answer += 1
        return answer

# 1047. Remove All Adjacent Duplicates In String
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack == [] or s[i] != stack[-1]:
                stack.append(s[i])
            else:
                stack.pop()
        return "".join(stack)

# 1078. Occurrences After Bigram
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        answer = []
        text = text.split(" ")
        for i in range(len(text)-2):
            if text[i] == first and text[i+1] == second:
                answer.append(text[i+2])
        return answer

# 1385. Find the Distance Value Between Two Arrays
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        answer = len(arr1)
        for i in arr1:
            for j in arr2:
                if abs(i - j) <= d:
                    answer -= 1
                    break
        return answer

# 1417. Reformat The String
class Solution:
    def reformat(self, s: str) -> str:
        answer = ""
        i = 0
        if len(s) == 1:
            return s
        numbers = [x for x in s if x.isnumeric()]
        string = [x for x in s if x.isalpha()]
        if s.isalpha() or s.isnumeric() or abs(len(numbers) - len(string)) >= 2:
            return answer
        if len(numbers) > len(string):
            shorter, longer = string, numbers
        else:
            shorter, longer = numbers, string
        while i < len(s):
            if i < len(longer):
                answer += longer[i]
            if i < len(shorter):
                answer += shorter[i]
            i += 1
        return answer

# 1491. Average Salary Excluding the Minimum and Maximum Salary
class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary) - max(salary) - min(salary)
        return total / (len(salary)-2)

# 1446. Consecutive Characters
class Solution:
    def maxPower(self, s: str) -> int:
        answer = 1
        count = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                count += 1
                if count > answer:
                    answer = count
            else:
                count = 1
        return answer

# 1903. Largest Odd Number in String
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""

# 1716. Calculate Money in Leetcode Bank
class Solution:
    def totalMoney(self, n: int) -> int:
        days = n % 7
        weeks = n // 7
        answer = 0
        for i in range(weeks):
            answer += 28 + (i*7)
        for i in range(1, days+1):
            answer += i + (weeks)
        return answer

# 1796. Second Largest Digit in a String
class Solution:
    def secondHighest(self, s: str) -> int:
        numbers = []
        for i in s:
            if i.isnumeric() and int(i) not in numbers:
                numbers.append(int(i))
        numbers = sorted(numbers)
        if len(numbers) < 2:
            return -1
        return numbers[-2]

# 1800. Maximum Ascending Subarray Sum
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = nums[0]
        temp = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                temp += nums[i]
                answer = max(temp, answer)
            else:
                temp = nums[i]
        return answer

# 2778. Sum of Squares of Special Elements
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            if len(nums) % (i + 1) == 0:
                answer += nums[i]**2
        return answer

# 2341. Maximum Number of Pairs in Array
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        map = {}
        answer = [0,0]
        for i in nums:
            map[i] = map.get(i,0) +1
        for k,v in map.items():
            answer[0] += v // 2
            answer[1] += v % 2
        return answer

# 2570. Merge Two 2D Arrays by Summing Values
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = 0
        map = {}
        while i < max(len(nums1), len(nums2)):
            if i < len(nums1):
                map[nums1[i][0]] = map.get(nums1[i][0], 0) + nums1[i][1]
            if i < len(nums2):
                map[nums2[i][0]] = map.get(nums2[i][0], 0) + nums2[i][1]
            i += 1
        return sorted([[k,v] for k,v in map.items()])

# 2357. Make Array Zero by Subtracting Equal Amounts
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        while sum(nums) != 0:
            nums = sorted(nums)
            for i in nums:
                if i != 0:
                    minVal = i
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = nums[i] - minVal
            answer += 1
        return answer

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        heapify(nums)

        while nums:
            if nums[0] == 0:
                heappop(nums)
            else:
                answer += 1
                nums = [x - nums[0] for x in nums]

        return answer

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = set()
        for i in nums:
            if i not in answer and i != 0:
                answer.add(i)
        return len(answer)

# 1403. Minimum Subsequence in Non-Increasing Order
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        if len(set(nums)) == 1:
            return nums
        for i in range(len(nums)):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums, reverse=True)
        for i in range(1,len(nums)):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]
        return nums

# 118. Pascal's Triangle
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []
        for i in range(1,numRows+1):
            if i <= 2:
                temp = [1] * i
            else:
                temp = [1] * i
                for i in range(1,len(temp)-1):
                    temp[i] = answer[-1][i] + answer[-1][i-1]
            answer.append(temp)
        return answer

# 2788. Split Strings by Separator
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for i in words:
            i = i.split(separator)
            for j in i:
                if j != "":
                    answer.append(j)
        return answer

# 2475. Number of Unequal Triplets in Array
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        answer += 1
        return answer

# 1779. Find Nearest Point That Has the Same X or Y Coordinate
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        answer = -1
        min_distance = float("inf")
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                if abs(x-points[i][0]) + abs(y-points[i][1]) < min_distance:
                    answer = i
                    min_distance = abs(x-points[i][0]) + abs(y-points[i][1])
        return answer

# 476. Number Complement
class Solution:
    def findComplement(self, num: int) -> int:
        binary = []
        answer = 0
        while num > 0:
            if num % 2 == 1:
                binary.append(0)
            else:
                binary.append(1)
            num = num // 2
        for i in range(len(binary)):
            answer += (binary[i]*2**i)
        return answer

# 191. Number of 1 Bits
class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n > 0:
            if n % 2 == 1:
                answer += 1
            n = n // 2
        return answer

class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        while n:
            if n & 1:
                answer += 1
            n = n >> 1
        return answer

# 190. Reverse Bits
class Solution:
    def reverseBits(self, n: int) -> int:
        binary = [0] * 32
        answer = 0
        i = 0
        while n > 0:
            binary[i] = n % 2
            n = n // 2
            i += 1
        binary = binary[::-1]
        for i in range(len(binary)):
            answer += (binary[i]*2**i)
        return answer

class Solution:
    def reverseBits(self, n: int) -> int:
        res=0
        for i in range(32):
            res=res<<1
            res+=n%2
            n=n>>1
        return res

# 1507. Reformat Date
class Solution:
    def reformatDate(self, date: str) -> str:
        month = {
            "Jan":"01",
            "Feb":"02",
            "Mar":"03",
            "Apr":"04",
            "May":"05",
            "Jun":"06",
            "Jul":"07",
            "Aug":"08",
            "Sep":"09",
            "Oct":"10",
            "Nov":"11",
            "Dec":"12"
        }
        date = date.split(" ")
        if len(date[0]) < 4:
            day = "0" + date[0][0]
        else:
            day = date[0][:2]
        answer = date[2] + "-" + month[date[1]] + "-" + day
        return answer

# 884. Uncommon Words from Two Sentences
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        answer = []
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        for i in s1:
            if s1.count(i) == 1 and s2.count(i) == 0:
                answer.append(i)
        for i in s2:
            if s2.count(i) == 1 and s1.count(i) == 0:
                answer.append(i)
        return answer

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        map = {}
        answer = []
        str = (s1 + " " + s2).split(" ")
        for i in str:
            map[i] = map.get(i,0) + 1
        for k,v in map.items():
            if v == 1:
                answer.append(k)
        return answer

# 2490. Circular Sentence
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
        for i in range(len(sentence)):
            if sentence[i] == " ":
                if sentence[i-1] != sentence[i+1]:
                    return False
        return True

# 2129. Capitalize the Title
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower()
        title = title.split(" ")
        answer = ""
        for i in title:
            if len(i) > 2:
                answer += i.capitalize() + " "
            else:
                answer += i + " "
        return answer[:-1]

# 868. Binary Gap
class Solution:
    def binaryGap(self, n: int) -> int:
        distance = []
        binary = []
        while n > 0:
            binary.append(n%2)
            n = n // 2
        flag = False
        temp = 0
        for i in binary:
            if flag and i == 1:
                distance.append(temp)
                temp = 0
                flag = False
            if i == 1:
                flag = True
            if flag:
                temp += 1
        if distance == []:
            return 0
        return max(distance)

# 2549. Count Distinct Numbers on Board
class Solution:
    def distinctIntegers(self, n: int) -> int:
        if n == 1:
            return 1
        return n-1

# 1331. Rank Transform of an Array
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        map = {}
        answer = []
        newarr = sorted(set(arr))
        for i in range(len(newarr)):
            map[newarr[i]] = i + 1
        for i in arr:
            answer.append(map[i])
        return answer

# 1995. Count Special Quadruplets
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        answer = 0
        if len(nums) < 4:
            return answer
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                for c in range(b+1,len(nums)):
                    for d in range(c+1,len(nums)):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            answer += 1
        return answer

# 2264. Largest 3-Same-Digit Number in String
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        answer = []
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                answer.append(int(num[i:i+3]))
        if answer == []:
            return ""
        elif max(answer) == 0:
            return "000"
        return str(max(answer))

# 383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}
        for i in magazine:
            map[i] = map.get(i,0) + 1
        for i in ransomNote:
            if map.get(i) == None:
                return False
            else:
                map[i] = map.get(i) -1
                if map[i] < 0:
                    return False
        return True

# 1399. Count Largest Group
class Solution:
    def countLargestGroup(self, n: int) -> int:
        map = {}
        answer = 0
        for i in range(1,n+1):
            temp = [int(x) for x in str(i)]
            if map.get(sum(temp)) == None:
                map[sum(temp)] = [i]
            else:
                map[sum(temp)].append(i)
        lengths = [len(v) for k,v in map.items()]
        max_num = max(lengths)
        for i in lengths:
            if i == max_num:
                answer += 1
        return answer

class Solution:
    def countLargestGroup(self, n: int) -> int:
        map = {}
        answer = 0
        max_num = 0
        for i in range(1,n+1):
            temp = [int(x) for x in str(i)]
            map[sum(temp)] = map.get(sum(temp),0) + 1
            if map[sum(temp)] > max_num:
                max_num = map[sum(temp)]
        for k,v in map.items():
            if v == max_num:
                answer += 1
        return answer

# 806. Number of Lines To Write String
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        answer = []
        temp = 0
        for i in s:
            i = ord(i)-97
            if widths[i] + temp <= 100:
                temp += widths[i]
            else:
                answer.append(temp)
                temp = 0
                temp += widths[i]
        answer.append(temp)
        return [len(answer),answer[-1]]

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        answer = []
        temp = 0
        for i in s:
            i = ord(i)-97
            if widths[i] + temp > 100:
                answer.append(temp)
                temp = 0
            temp += widths[i]
        return [len(answer)+1,temp]

# 429. N-ary Tree Level Order Traversal
# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        answer = defaultdict(list)

        def dfs(node, level):
            if not node:
                return
            answer[level].append(node.val)
            for i in node.children:
                dfs(i,level+1)
        
        dfs(root,0)

        return [lst for k,lst in answer.items()]

# 589. N-ary Tree Preorder Traversal
# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []

        def traversal(node):
            if not node:
                return
            answer.append(node.val)
            for i in node.children:
                traversal(i)
        
        traversal(root)

        return answer

# 590. N-ary Tree Postorder Traversal
# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answer = []

        def traversal(node):
            if node:
                for i in node.children:
                    traversal(i)
                answer.append(node.val)

        traversal(root)
        return answer

# 1876. Substrings of Size Three with Distinct Characters
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        answer = 0
        for i in range(len(s)-2):
            if s[i] != s[i+1] and s[i] != s[i+2] and s[i+1] != s[i+2]:
                answer += 1
        return answer

# 1394. Find Lucky Integer in an Array
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        answer = -1
        map = {}
        for i in arr:
            map[i] = map.get(i,0) + 1
        for k, v in map.items():
            if k == v and k > answer:
                answer = k
        return answer

# 1380. Lucky Numbers in a Matrix
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_nums = []
        answer = []
        for i in matrix:
            min_nums.append(min(i))
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                temp.append(matrix[j][i])
            if (max(temp)) in min_nums:
                answer.append(max(temp))
        return answer

# 965. Univalued Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        node_vals = []
        def traversal(node):
            if not node:
                return
            node_vals.append(node.val)
            traversal(node.left)
            traversal(node.right)
        traversal(root)
        check = node_vals[0]
        for i in node_vals:
            if i != check:
                return False
        return True

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left != None and root.left.val != root.val:
            return False
        if root.right != None and root.right.val != root.val:
            return False
        
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)

# 2224. Minimum Number of Operations to Convert Time
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        times = [60,15,5,1]
        current_min = int(current[0:2]) * 60 + int(current[3:5])
        correct_min = int(correct[0:2]) * 60 + int(correct[3:5])
        diff = correct_min - current_min

        answer = 0
        for i in times:
            while diff >= i:
                answer += 1
                diff -= i
        return answer

# 2706. Buy Two Chocolates
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices = sorted(prices)
        if prices[0] + prices[1] <= money:
            return money - (prices[0] + prices[1])
        return money

# 2347. Best Poker Hand
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        hand = {}
        if len(set(suits)) == 1:
            return "Flush"
        for i in ranks:
            hand[i] = hand.get(i,0) + 1
        answer = "High Card"
        for k,v in hand.items():
            if v >= 3:
                answer = "Three of a Kind"
            elif v == 2 and answer == "High Card":
                answer = "Pair"
        return answer

# 1009. Complement of Base 10 Integer
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = []
        answer = 0
        if n == 0:
            return 1
        while n > 0:
            if n%2 == 1:
                binary.append(0)
            else:
                binary.append(1)
            n = n // 2
        for i in range(len(binary)):
            answer += (binary[i]*2**i)
        return answer

# 1539. Kth Missing Positive Number
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        key = []
        for i in range(1,max(arr)+k+1):
            if len(key) == k:
                break
            if i not in arr:
                key.append(i)
        return key[-1]

# 2451. Odd String Difference
class Solution:
    def oddString(self, words: List[str]) -> str:
        key = []
        for i in range(len(words)):
            temp = []
            for j in range(len(words[i])-1):
                difference = ord(words[i][j+1]) - ord(words[i][j])
                temp.append(difference)
            key.append(temp)
        index = 0
        for i in range(len(key)):
            if key.count(key[i]) == 1:
                index = i
        return words[index]

# 2299. Strong Password Checker II
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        validation = set()
        special = "!@#$%^&*()-+"

        if len(password) < 8:
            return False

        def check(c):
            if c in special:
                validation.add(1)
            elif c.isupper():
                validation.add(2)
            elif c.islower():
                validation.add(3)
            elif c.isnumeric():
                validation.add(4)

        for i in range(len(password)-1):
            if password[i] == password[i+1]:
                return False
            check(password[i])
        check(password[-1])
        
        return len(validation) == 4

# 1496. Path Crossing
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        route = [[0,0]]
        for i in path:
            temp = route[-1]
            if i == "N":
                temp = [temp[0]+1,temp[1]]
            elif i == "S":
                temp = [temp[0]-1,temp[1]]
            elif i == "E":
                temp = [temp[0],temp[1]+1]
            elif i == "W":
                temp = [temp[0],temp[1]-1]
            if temp in route:
                return True
            route.append(temp)
        return False

# 2798. Number of Employees Who Met the Target
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        answer = 0
        for i in hours:
            if i >= target:
                answer += 1
        return answer

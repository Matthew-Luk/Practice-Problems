from typing import List, Optional, ListNode, Node
from collections import defaultdict
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
        print(rows)
        print(cols)
        result = 0
        for i in range(rows):
            grid[i] = sorted(grid[i])[::-1]
        for j in range(cols):
            temp = []
            for i in range(rows):
                temp.append(grid[i][j])
            result += max(temp)
        return result

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

# 2485. Find the Pivot Integer
class Solution:
    def pivotInteger(self, n):
        newList = list(range(1,n+1))
        for i in range(len(newList)):
            if sum(newList[:i+1]) == sum(newList[i:]):
                return newList[i]
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
        print(nums)
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
        print(answer)
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

# 1822. Sign of the Product of an Array
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for i in nums:
            product *= i
        return 1 if product > 0 else (-1 if product < 0 else 0)

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

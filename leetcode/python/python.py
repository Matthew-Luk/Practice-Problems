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
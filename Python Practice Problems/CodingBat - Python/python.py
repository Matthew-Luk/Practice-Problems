# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
def sleep_in(weekday, vacation):
    return weekday == False or vacation == True


# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile


# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
def sum_double(a, b):
    if a == b:
        return ((a+b)*2)
    return a+b


# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
def diff21(n):
    if n <= 21:
        return 21-n
    return (n-21) * 2


# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
def parrot_trouble(talking, hour):
    if hour < 7 or hour > 20:
        return talking
    return False


# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a, b):
    return a == 10 or b == 10 or a+b == 10


# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
def near_hundred(n):
    return n >= 190 and n <= 210 or n >= 90 and n <= 110


#Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    return a < 0 and b >= 0 or a >= 0 and b < 0


# Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
def not_string(str):
    if str.startswith("not"):
        return str
    return ("not "+str)


#  Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive)
def missing_char(str, n):
    return str[:n] + str[n+1:]


# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
    if len(str) <= 1:
        return str
    return str[-1] + str[1:-1] + str[0]


# Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.
def front3(str):
    return str[:3]*3


# Given a string and a non-negative int n, return a larger string that is n copies of the original string.
def string_times(str, n):
    return str*n


# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;
def front_times(str, n):
    return str[:3]*n


# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
    return str[::2]


# Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(str):
    x = []
    for i in range(len(str)+1):
        x.append(str[:i])
        i += 1
    return ("".join(x))


# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(str):
    x = 0
    for i in range(len(str)-2):
        if str[i] + str[i+1] == str[-2:]:
            x += 1
    return x


# Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
    x = 0
    for i in range(len(nums)):
        if nums[i] == 9:
            x += 1
    return x

def array_count9(nums):
    return nums.count(9)


# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.
def array_front9(nums):
    nums = nums[:3]
    return nums.count(9) > 0


# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
def array123(nums):
    for i in range(len(nums)-2):
        if nums[i] == 1:
            if nums[i+1] == 2:
                if nums[i+2] == 3:
                    return True
    return False


# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
def string_match(a, b):
    shorter = min(len(a), len(b))
    count = 0
    for i in range(shorter-1):
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub == b_sub:
            count = count + 1
    return count


# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
def hello_name(name):
    return "Hello " + name + "!"


# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
def make_abba(a, b):
    return a + b + b + a


# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
def make_tags(tag, word):
    return "<"+tag+">"+word+"<"+"/"+tag+">"


# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
def make_out_word(out, word):
    return out[:2] + word + out[-2:]


# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.
def extra_end(str):
    return str[-2:]*3


# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
def first_two(str):
    return str[:2]


# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
def first_half(str):
    return str[:len(str)/2]


# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.
def without_end(str):
    return str[1:-1]


# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).
def combo_string(a, b):
    if len(a) < len(b):
        return a+b+a
    return b+a+b



# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.
def non_start(a, b):
    return a[1:] + b[1:]


# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.
def left2(str):
    return str[2:] + str[:2]


# Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
def first_last6(nums):
    return nums[0] == 6 or nums[-1] == 6


# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
def same_first_last(nums):
    return len(nums) >= 1 and nums[0] == nums[-1]


# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
def make_pi():
    return [3,1,4]


# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]


# Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
    return sum(nums)


# Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
def rotate_left3(nums):
    return [nums[1],nums[2],nums[0]]


# Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
def reverse3(nums):
    return nums[::-1]


# Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
def max_end3(nums):
    if nums[0] > nums[-1]:
        return [nums[0],nums[0],nums[0]]
    return [nums[-1],nums[-1],nums[-1]]


# Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
def sum2(nums):
    if len(nums) >= 2:
        return nums[0]+nums[1]
    elif len(nums) == 1:
        return nums[0]
    return 0


# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
def middle_way(a, b):
    return [a[1],b[1]]


# Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
def make_ends(nums):
    return [nums[0],nums[-1]]


# Given an int array length 2, return True if it contains a 2 or a 3.
def has23(nums):
    return(nums.count(2) > 0 or nums.count(3) > 0)


# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
def cigar_party(cigars, is_weekend):
    return (cigars >= 40 and cigars <= 60 or cigars >= 40 and is_weekend)


# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
def date_fashion(you, date):
    if(you <= 2 or date <=2):
        return 0
    elif(you >= 8 or date >= 8):
        return 2
    return 1


# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
def squirrel_play(temp, is_summer):
    return(temp >= 60 and temp <= 90 or temp >= 60 and temp <= 100 and is_summer) 


# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
    if(speed <= 60 or is_birthday and speed <= 65):
        return 0
    elif(speed >= 61 and speed <= 80 or is_birthday and speed >= 61 and speed <=85):
        return 1
    return 2


# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
def sorta_sum(a, b):
    x = (a+b)
    if x >= 10 and x <= 19:
        return 20
    return x


# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
def alarm_clock(day, vacation):
    if(day >= 1 and day <= 5 and not vacation):
        return "7:00"
    elif(day == 6 and not vacation or day == 0 and not vacation or day >= 1 and day <= 5 and vacation):
        return "10:00"
    return "off"


# The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
def love6(a, b):
    return(a == 6 or b == 6 or (a+b) == 6 or abs(a-b) == 6)


# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
def in1to10(n, outside_mode):
    if outside_mode == True:
        return(n<=1 or n>=10)
    return (n>=1 and n<=10)


# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod
def near_ten(num):
    return(num%10 >= 8 or num%10 <= 2)


# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks



# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
def lone_sum(a, b, c):
    x = [a, b, c]
    y = sum(x)
    for i in range(len(x)):
        if x.count(x[i]) > 1:
            y = y - (x.count(x[i]) * x[i])
        return y
    return y

# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
def lucky_sum(a, b, c):
    x = [a,b,c]
    if x.count(13) > 0:
        y = x.index(13)
        x = x[:y]
    return sum(x)


# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().
def no_teen_sum(a, b, c):
    return (fix_teen(a) + fix_teen(b) + fix_teen(c))

def fix_teen(n):
    if n >= 13 and n <= 19:
        if n <= 14:
            n = 0
        elif n >= 17:
            n = 0
    return n


# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().
def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)

def round10(num):
    if num % 10 < 5:
        num = num - (num%10)
    elif num % 10 >= 5:
        num = num + (10 - (num%10))
    return num

# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
def close_far(a, b, c):
    return abs(b-a) <= 1 and abs(c-a) >= 2 and abs(c-b) >= 2 or abs(c-a) <= 1 and abs(b-a) >= 2 and abs(b-c) >= 2


# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.


# Given a string, return a string where for every char in the original, there are two chars.
def double_char(str):
    x = ""
    for i in range(len(str)):
        x = x + str[i] + str[i]
    return x


# Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
    x = 0
    for i in range(len(str)-1):
        if str[i] == "h" and str[i+1] == "i":
            x += 1
    return x


# Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
    x = 0
    y = 0
    for i in range(len(str)-2):
        if str[i] == "c" and str[i+1] == "a" and str[i+2] == "t":
            x += 1
        elif str[i] == "d" and str[i+1] == "o" and str[i+2] == "g":
            y += 1
    return x == y


# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
    x = 0
    for i in range(len(str)-3):
        if str[i] == "c" and str[i+1] == "o" and str[i+3] == "e":
            x += 1
    return x


# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)


# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
def xyz_there(str):
    if str.count(".") == 1:
        x = str.index(".")
        return str[x+2:].count("xyz") > 0 or str[:x].count("xyz") > 0
    elif str.count(".") > 1:
        return str.count(".xyz") != str.count("xyz")
    return str.count("xyz") > 0

def xyz_there(str):
    return str.count(".xyz") != str.count("xyz")


# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
def count_evens(nums):
    x = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            x += 1
    return x

# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
def big_diff(nums):
    return max(nums) - min(nums)

# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more
def centered_average(nums):
    nums = sorted(nums)
    if len(nums) % 2 == 1:
        return nums[len(nums)/2]
    return ((nums[len(nums)/2] + nums[(len(nums)/2)-1]) / 2)

# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.


# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.


# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(nums):
    x = 0
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            x += 1
    return x > 0
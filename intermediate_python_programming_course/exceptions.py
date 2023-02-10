# Errors and Exceptions

# module error
# import somemodule

# type error
# a = 5 + "10"

# syntactic error
# a = 5
# print(a))

# name error
# a = 5
# b = c

# file error
# f = open("somefile.txt")

# value error
# a = [1,2,3]
# a.remove(4)

# index error
# a = [1,2,3]
# a[4]

# assertion error
# x = 5
# assert (x>=0), "x is not positive"

# raise exceptions
# x = -5
# if x < 0:
#     raise Exception("x should be positive")

# try:
#     a = 5 / 1
#     b = a + 10
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("everything is fine")
# finally:
#     print("cleaning up...")

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self,message,value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value is too small", x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
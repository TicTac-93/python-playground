# Coding Bat warmups

# ------------------
# sleep_in
# ------------------

def sleep_in(weekday, vacation):
    # type: (bool, bool) -> bool
    """
    Output True if it's not a weekday OR we're on vacation.
    """

    return weekday is False or vacation is True



# Test sleep_in()
print("Testing sleep_in()...")
print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))
print


# ------------------
# diff21
# ------------------

def diff21(n):
    # type: (int) -> int
    """
    Return the absolute difference between n and 21.
    Return double that if n is over 21.
    """

    diff = abs(n - 21)
    if n > 21:
        diff = diff*2

    return diff


# Test diff21()
print("Testing diff21()...")
print(diff21(19))
print(diff21(10))
print(diff21(21))
print(diff21(25))
print


# ------------------
# missing_char
# ------------------

def missing_char(str, index):
    # type: (str, int) -> str
    """
    Return a string with the character at index n removed.
    """

    if index >= len(str) or index < 0:
        print("Index value is out of range!")
        return ""
    else:
        output = str[:index] + str[index+1:]
        return output


# Test missing_char()
print("Testing missing_char()...")
print(missing_char('kitten', 1))
print(missing_char('kitten', 0))
print(missing_char('kitten', 4))
print(missing_char('kitten', 5))
print(missing_char('kitten', 10))
print


# ------------------
# pos_neg
# ------------------

def pos_neg(a, b, negative):
    # type: (int, int, bool) -> bool
    """
    Return True if one value is negative and one is positive.
    If param 'negative' is True, only return True if both are negative.
    """

    if negative:
        return a < 0 and b < 0
    elif a < 0:
        return b > 0
    elif a > 0:
        return b < 0


# Test pos_neg()
print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))
print(pos_neg(10, 7, False))
print


# ------------------
# front_back
# ------------------

def front_back(str):
    # type: (str) -> str
    """
    Returns a string with the first and last characters swapped.
    """

    if len(str) == 1:
        return str

    strlength = len(str)
    return str[strlength-1:] + str[1:strlength-1] + str[:1]


# Test front_back
print(front_back('code'))
print(front_back('a'))
print(front_back('ab'))
print


# ------------------
# not_string
# ------------------

def not_string(str):
    # type: (str) -> str
    """
    Return the string with 'not' prepended to it.  If it already begins with 'not', return it unchanged.
    """

    if str[:3] == 'not':
        return str
    else:
        return 'not ' + str


# Test not_string
print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))
print


# ------------------
# string_times
# ------------------

def string_times(str, n):
    # type: (str, int) -> str
    """
    Take an input string, and output it concatenated n-times.
    """

    output = ''
    for x in range(n):
        output = output + str

    return output


# Test string_times
print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Hi', 1))
print


# ------------------
# string_splosion
# ------------------

def string_splosion(str):
    """
    Return the input string as [:1][:2][:3]...etc.
    If the string is empty, return nothing.
    """

    if len(str) == 0:
        return

    output = ''
    for x in range(len(str)):
        output = output + str[:x+1]

    return output


# Test string_splosion
print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))
print(string_splosion('x'))
print(string_splosion(''))
print


# ------------------
# first_last6
# ------------------

def first_last6(nums):
    """
    Return True if 6 appears as either the first or last element in the array
    """

    return nums[0] == 6 or nums[len(nums)-1] == 6


# Test first_last6
print(first_last6([1,2,6]))
print(first_last6([6,1,2,3]))
print(first_last6([13,6,1,2,3]))
print


# ------------------
# rotate_left3
# ------------------

def rotate_left3(nums):
    """
    Return the input array with values shifted 'left', ie [0,1,2,3] -> [1,2,3,0]
    """

    first = nums[0]
    output = nums[1:]
    output.append(first)

    return output


# Test rotate_left3
print(rotate_left3([1, 2, 3]))
print(rotate_left3([0, 1, 2, 3, 4, 5]))
print(rotate_left3([0, 1]))
print(rotate_left3([0]))
print

# # 05 - Glad to be One

# ## Problem Statement


# _The Glad to be One number sequence are those whose sequence ends in a one. Numbers that are not “glad” are those that infinitely repeat a sequence of numbers but never reach the number one. For this problem you must determine if a number is a glad number or not. For a given positive integer $N$, the next number in the sequence will be the sum of the squares of its digits. Continue to generate numbers in the sequence until the sequence reaches one or the sequence begins to repeat itself. The original input is a glad number if the sequence reaches one. The original input is not a glad number if the sequence starts to repeat itself without reaching one._


# ## Input Format:
# - int

# ## Output Format:
# - bool (True if Glad Number | False if Not a Glad Number)

# ## Constraints:
# - Input will always be a positive integer

# ## Sample:

# | Input | Output |
# | ----- | ------ |
# | 49    | True   |
# | 11    | False  |
# | 97    | True   |
# | 1234  | False  |

# ### Explanation:

# 49 is a glad number because:

# Sequence generated:
# $49 -> 97 -> 130 -> 10 -> 1$

# Output: True

# The sequence was generated as follows:

# $4^2 + 9^2 = 97$

# $9^2 + 7^2 = 130$

# $1^2 + 3^2 + 0^2 = 10$

# $1^2 + 0^2 = 1$

# ---

# 11 is not a glad number because:

# Output: False

# The sequence was generated as follows:

# $1^2 + 1^2 = 2$

# $2^2 = 4$

# $4^2 = 16$

# $1^2 + 6^2 = 37$

# $3^2 + 7^2 = 58$

# $5^2 + 8^2 = 89$

# $8^2 + 9^2 = 145$

# $1^2 + 4^2 + 52 = 42$

# $4^2 + 2^2 = 20$

# $2^2 + 0^2 = 4$

# Sequence will repeat and not reach 1

# Write your code in the function labeled `answer()` below
###########################################################


def answer(number: int) -> bool:
    dig = get_dig(number)
    repeats = []
    print("----")
    print(f"input = {number}")

    while True:
        s = 0
        for d in dig:
            s += d * d
        print(s)
        if s == 1:
            return True
        else:
            if s in repeats:
                return False
        repeats.append(s)
        dig = get_dig(s)


def get_dig(num):
    a = []
    s = str(num)
    l = list(s)
    for d in l:
        a.append(int(d))
    return a

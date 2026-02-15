#   # 03 - Remove the vowels!

#   ## Problem Statement


#   _You are getting attacked by evil Trolls. Remove their power by removing the vowels from their comments._


#   > Note: For this problem, `y` isn't considered a vowel.

#   ## Input Format:
#   - String

#   ## Output Format:
#   - String

#   ## Constraints:
#   - Vowels are considered `a`, `e`, `i`, `o`, `u`

#   ## Sample:

#   | Input | Output |
#   | ----- | ------ |
#   | Hello | Hll    |

#   ### Explanation:

#   None


# Write your code in the function labeled `problem()` below
###########################################################


def answer(inp) -> None:
    inp = inp.replace("a", "")
    inp = inp.replace("e", "")
    inp = inp.replace("i", "")
    inp = inp.replace("o", "")
    inp = inp.replace("u", "")
    inp = inp.replace("A", "")
    inp = inp.replace("E", "")
    inp = inp.replace("I", "")
    inp = inp.replace("O", "")
    inp = inp.replace("U", "")

    return inp

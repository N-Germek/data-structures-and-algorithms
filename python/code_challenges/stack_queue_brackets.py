from data_structures.stack import Stack, Node


# char_dict =
#     {
#     letter = { 1: "A",
#                2: "a",
#                3:"B",
#                4: "b",
#                5: "C",
#                6: "c",
#                7: "D",
#                8: "d",
#                9: "E",
#                10: "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m",
#                "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v",
#                "W", "w", "X", "x", "Y", "y", "Z", "z"
#     }
# }
# string_input = ""
brackets = ["[", "]", "(", ")", "{", "}"]


def is_palindrome(chars):
    return chars == chars[::-1]


def multi_bracket_validation(str_input):
    bracket_stack = []
    skipped_chars = []
    while str_input is not None:
        for char in str_input:
            if char == len(brackets):
                bracket_stack.Stack.push(char)
            elif char != len(brackets):
                skipped_chars.Stack.push(char)
                char = char.next
    if bracket_stack is not None:
        if bracket_stack == is_palindrome(bracket_stack):
            return True
        else:
            return False
    breakpoint()

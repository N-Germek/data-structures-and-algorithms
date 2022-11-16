brackets = ["[", "]", "(", ")", "{", "}"]


def multi_bracket_validation(string):
    bracket_palindrome = {'(': ')', '[': ']', '{': '}'}
    # set is storing multiple things in a single variable
    pairs = set(['(', '[', '{'])
    # create storage variable
    storage = []
    # loop through string
    for i in string:
        # search for any pairs variable
        if i in pairs:
            # append any of the pairs variable to the storage stack
            storage.append(i)
        # if the character from storage and string match, remove them from storage
        elif storage and i == bracket_palindrome[storage[-1]]:
            storage.pop()
        else:
            return False
    # handle once storage is empty and palindrome has been confirmed, return boolean
    if len(storage) == 0:
        return True
    else:
        return False

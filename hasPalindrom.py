def hasPalindrome(word):
    # we make set to check only one value can appear odd number of times
    characterSet = set()

    for char in word:

        # if char is present in set then remove it (it means iit have even appearance)
        if char in characterSet:
            characterSet.remove(char)
        else:
            # if character is not in set means it has odd number apperance
            characterSet.add(char)

    # now if set is empty or have only one character it means that there exists a one permutation
    #  of word which is palindrome
    return len(characterSet) <= 1
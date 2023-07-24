class WordCloud:
    
    def __init__(self):
        self.wordsCount = {}
        self.wordsList = []

    def addToDictionary(self, word):
        # if word is already there increment it
        if word in self.wordsCount:
            self.wordsCount[word] += 1
        # if word is present but in lowercase,
        # as we are storing only Pronouns words always with capital letter first
        # so we store them as lower
        elif word.lower() in self.wordsCount:
            self.wordsCount[word] += 1
        # if word is present but in capitalize form 
        # we add that value to new key storing that word with lowercase key
        elif word.capitalize() in self.wordsCount:
            self.wordsCount[word] = 1 + self.wordsCount[word.capitalize]
            del self.wordsCount[word.capitalize]
        # if it is a new key then add it to dictionary
        else:
            self.wordsCount[word] = 1

    def splitAndPopulateDictionary(self, message):
        startIndex = 0
        wordLength = 0
        for i, char in enumerate(message):
            # If we reached the end of the string we check if the last
            # character is a letter and add the last word to our dictionary
            if i == len(message) - 1:
                if char.isalpha():
                    wordLength += 1
                if wordLength > 0:
                    word = message[startIndex: startIndex + wordLength]
                    self.addToDictionary(currentWord)

            # If we reach a space or emdash we know we're at the end of a word
            # so we add it to our dictionary and reset our current word
            elif char == ' ' or char == '\u2014':
                if wordLength > 0:
                    currentWord = message[startIndex:startIndex + wordLength]
                    self.addToDictionary(currentWord)
                    wordLength = 0

            # We want to make sure we split on ellipses so if we get two periods in
            # a row we add the current word to our dictionary and reset our current word
            elif char == '.':
                if i < len(message) - 1 and message[i + 1] == '.':
                    if wordLength > 0:
                        currentWord = message[startIndex:startIndex + wordLength]
                        self.addToDictionary(currentWord)
                        wordLength = 0

            # If the character is a letter or an apostrophe, we add it to our current word
            elif char.isalpha() or char == '\'':
                if wordLength == 0:
                    startIndex = i
                wordLength += 1

            # If the character is a hyphen, we want to check if it's surrounded by letters
            # If it is, we add it to our current word
            elif char == '-':
                if i > 0 and message[i - 1].isalpha() and message[i + 1].isalpha():
                    wordLength += 1
                else:
                    if wordLength > 0:
                        currentWord = message[startIndex:startIndex + wordLength]
                        self.addToDictionary(currentWord)
                        wordLength = 0
        print(self.wordsCount)

word = WordCloud()

word.splitAndPopulateDictionary(  'Cliff finished-his cake and paid the bill.'
'Bill finished his cake at the edge of the cliff.')
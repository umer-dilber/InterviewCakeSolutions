def reversWords(msg):
    # first reverse whole sring
    reverseString(msg, 0, len(msg)-1)

    # then reverse each word 
    start = 0
    for i in range(len(msg)+1):
        # if character at index (i) is space or end of list it means a word then revese it
        if(i == len(msg)) or (msg[i] == ' '):
            reverseString(msg, start, i-1)
            start = i+1


def reverseString(msg, leftIndex, rightIndex):
    while(leftIndex<rightIndex):
        msg[leftIndex], msg[rightIndex] = msg[rightIndex], msg[leftIndex]
        leftIndex += 1
        rightIndex -= 1
    return str


message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]
reversWords(message)
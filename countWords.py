def wordcounting(txt):
    wordcount = dict()
    wordsplit = txt.split()
    for item in wordsplit:
        if item in wordcount:
            wordcount[item] += 1
        else:
            wordcount[item] = 1
    return wordcount

file = open('words.txt', 'r')
data = file.read()
print('File data:\n' + data)
finalresult = wordcounting(data)
print(finalresult)

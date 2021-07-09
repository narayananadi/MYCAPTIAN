def most_frequent(wordstr):
    x = 0
    dictof = {}
    while x < len(wordstr):
        if wordstr[x] in dictof:
            item = dictof[wordstr[x]]
            item += 1
            dictof[wordstr[x]] = item
        else:
            dictof[wordstr[x]] = 1
        x += 1
    return dictof


word = str(input("enter the word :"))
returndict = most_frequent(word.lower())

sort_dict = sorted(returndict.items(), key=lambda x: x[1], reverse=True)
for i in sort_dict:
    print(i[0], " = ", i[1])

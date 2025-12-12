f = open('sampleText.txt', 'r')
temp = f.read()

content = (temp.split())
print(content)
wordCount = {}

for i in content:
    if i not in wordCount:
        wordCount[i] = 1
    else:
        wordCount[i] += 1

print(wordCount)
v = wordCount.values()
v = list(v)
k = wordCount.keys()
k = list(k)

for i in range (len(v)):
    if int(v[i]) > 1:
        print(k[i], v[i])
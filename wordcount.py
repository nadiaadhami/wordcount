# count the number of words in a file and return the word with the largest frequency
# input: hamlet.txt

name = input("enter file name: ")
fp = open(name, "r")

counts = dict()
for line in fp:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

maxword = None
maxcount = None

for word,count in counts.items():
    if maxcount is None or count > maxcount:
      maxword = word
      maxcount = count

print(maxword, maxcount)


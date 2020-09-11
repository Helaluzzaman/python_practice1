fname= input("Enter text file name which you want to analyze:")
if len(fname) <2:
    fname = "mbox-short.txt"
fh = open(fname)

text = fh.read()
totalletters = len(text)
#print(totalletters)
def match(char):
    count=0
    for c in text:
        if char == c:
            count = count +1
    return count

letters = list()
for c in text:
    if c == " " or c =="\n" or c == "\t":
        continue
    if c not in letters:
        letters.append(c)
#print(letters)
ddd = dict()
for char in letters:
    numchar = match(char)
    percent = 100 * numchar/totalletters
    ddd[char] = percent
srtedlist = sorted([(p,c) for c,p in ddd.items()],reverse=True)

for p,c in srtedlist[:100]:
    print(" '{0}' : {1}%".format(c, round(p,2)))

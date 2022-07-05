phrase = 'Take only the words that start with t in this sentence'
a=[i for i in phrase.split() if i[0]=='T' or i[0]=='t']
print(a)
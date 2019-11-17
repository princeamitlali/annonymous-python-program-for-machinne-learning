import nltk
from nltk.tokenize import word_tokenize
#nltk.download()
with open("FILE_YOU_WANT_TO_OPEN.txt", "r") as f:
	text = f.read()
print("Document opened!")
tokenized_word=word_tokenize(text)
print("tokenized_word")
from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
y = fdist.most_common(10000)

k = 0
with open("most_common.txt", "w") as f:
	for i, j in y:
		k += 1
		if k<20: print(f"i: {i.encode('ascii', 'backslashreplace')}, j: {j}")
		f.write(i+"\n")

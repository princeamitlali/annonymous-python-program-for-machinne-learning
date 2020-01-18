import nltk
from nltk.tokenize import word_tokenize
import glob
import json
import os

files = glob.glob("/home1/santosh/Praveen/VG_Hindi/1.2/val_gt_regions/*.json")
for file in files:
	with open(file,"r") as fp:
		js = json.load(fp)
for element in js['regions']:
	x = element['phrase']
	y = word_tokenize(x)
		element['phrase_tokens'] = y[:8]

	with open(file,"w") as nf:
		json.dump(js, nf)

	

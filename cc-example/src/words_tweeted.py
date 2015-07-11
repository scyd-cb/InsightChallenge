#!/usr/bin/env python

import sys


if __name__ == "__main__":
	inpath = sys.argv[1]
	outpath = sys.argv[2]
	txt = open(inpath)
	dictionary = {}
	count = 0
	for tweet in txt.readlines():
		count += 1
		for word in tweet.split():
			if word in dictionary:
				dictionary[word] += 1
			else:
				dictionary[word] = 1
	
	txt.close()

	# create output file 
	out = open(outpath, 'w')

	for key in  sorted(dictionary.iterkeys()):
		out.write("{0:25} {1}".format(key, dictionary[key]) + "\n")
	out.close()

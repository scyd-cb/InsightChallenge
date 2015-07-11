#!/usr/bin/env python

import sys


if __name__ == "__main__":
        inpath = sys.argv[1]
	outpath = sys.argv[2]
        txt = open(inpath)
        out = open(outpath, 'w')
        dictionary = {}
        total  = 0.00
	tweetCount = 0.00
        for tweet in txt.readlines():
		tweetCount += 1
		checked = {}
		count = 0.00
                
		for word in tweet.split():
			#check if if word has been couted more than once
			if word in checked.keys():	
				if checked[word] == 1: checked[word] -= 1
				checked[word] += 1
			else:
				count += 1
				checked[word] = 1
		
		total += count
		# write median to output file
		out.write( "%.2f" %(total/tweetCount) + "\n")
	out.close()
	txt.close()

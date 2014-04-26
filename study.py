#!/usr/bin/env python

import sys					# for system io
import sqlite3					# for DB Activities
import urllib2					# for url parssing et al
import textwrap					# To limit o/p characters per line
import subprocess				# To invoke espeak
import time
from nltk.corpus import wordnet as wn		# Wordnet DB
from nltk.stem.wordnet import WordNetLemmatizer	# To Obtain Lemma
from BeautifulSoup import BeautifulSoup		

def print_summary():
	print "\n \
		This module can be used to study words in list. \n \
		Usage : \n \
	 	$ "+ sys.argv[0] +" input_file \n \
			input_file : text file containing list of words \
	" 

if __name__ == "__main__":

	# Input arguments check
	if(len(sys.argv) != 2):
		print_summary()
		sys.exit()

	known = 0
	studied = 0
	words = 0
	espeak_cmd = 'espeak  -s 150 -v en-us+f5 '

	l = WordNetLemmatizer()

	try:
		fp = open(sys.argv[1],'r')
		wlist = fp.read()
	except:
		wlist = sys.argv[1]

	for word in wlist.split():
		words = words + 1
	print "Total words : %d" %(words)

	for word in wlist.split():
		if len(wn.synsets(word)) is not 0:
			rlemma = l.lemmatize(word)
			subprocess.call( espeak_cmd +"'"+word+"'", shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
			opt = raw_input( "Display %s : %s?  :   " % (word,l.lemmatize(word)))
			if opt == 'p':
				studied = studied+1
				for ss in wn.synsets(word):
					print "%20s : %s\n" % (word,ss.definition)
					time.sleep(0.5)
			if opt == 's':
				studied = studied+1
				for ss in wn.synsets(word):
					print "%20s : %s\n" % (word,ss.definition)
					subprocess.call(espeak_cmd +"'"+ss.definition+"'", shell=True, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
					time.sleep(0.5)
			if opt == 'e':
			  	print "Current streak : %d %d" % (studied,known)
				sys.exit()
			if opt == 'm':
				studied = studied+1
				for ss in wn.synsets(word):
					print "%20s : %s\n" % (word,ss.definition)
			  	url="http://www.vocabulary.com/dictionary/"+word
				response = urllib2.urlopen(url)
				replace = ["\"","<i>","</i>","<p class=long>","<p class=short>","</p>"]
				html = response.read()
				soup = BeautifulSoup(html)
				rshort = soup.findAll(attrs={"class" : "short"})
				rlong = soup.findAll(attrs={"class" : "long"})
				rlong = str(rlong[0])
				rshort = str(rshort[0])
				for rep in replace:
					rlong=rlong.replace(rep,"")
					rshort = rshort.replace(rep,"")
				print "%s\n\n%s\n\n" % (textwrap.fill(rshort, width=100),textwrap.fill(rlong, width=100))
			else:
				known = known+1

	
	print "Current streak : %d %d" % (studied,known)
	sys.exit()

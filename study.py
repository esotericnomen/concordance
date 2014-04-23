import sys
from nltk.corpus import wordnet as wn
from nltk.stem.wordnet import WordNetLemmatizer

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

	fp = open(sys.argv[1],'r')
	l = WordNetLemmatizer()

	barrons = fp.read()
	for word in barrons.split():
		words = words + 1
	print "Total words : %d" %(words)

	for word in barrons.split():
		if len(wn.synsets(word)) is not 0:
			rlemma = l.lemmatize(word)
			opt = raw_input( "Display %s : %s?  :   " % (word,l.lemmatize(word)))
			if opt == 'y':
				studied = studied+1
				for ss in wn.synsets(word):
					print "%20s : %s\n" % (word,ss.definition)
			if opt == 'e':
			  	print "Current streak : %d %d" % (studied,known)
				sys.exit()
			else:
				known = known+1

	
	print "Current streak : %d %d" % (studied,known)
	sys.exit()

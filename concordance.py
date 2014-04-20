#! /usr/bin/env python
# coding: utf-8
"""
##############################################################################
# Description : This module reads the I/P document and prints		     #
# 		# Meaningful unique words 				     #
# 		# Count of occurance in the document and		     #
# 		# Number of senses  					     #
# Author 	    : Rajkumar Ramasamy [rraj.be@gmail.com]		     #
##############################################################################
@  This program is free software: you can redistribute it and/or modify	     @
@  it under the terms of the GNU General Public License as published by	     @
@  the Free Software Foundation, either version 3 of the License, or	     @
@  (at your option) any later version.					     @
@									     @
@  This program is distributed in the hope that it will be useful,	     @
@  but WITHOUT ANY WARRANTY; without even the implied warranty of	     @
@  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the	     @
@  GNU General Public License for more details.				     @
@									     @
@  You should have received a copy of the GNU General Public License	     @
@  along with this program.  If not, see <http://www.gnu.org/licenses/>.     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
import sys
from nltk.corpus import wordnet as wn
def print_summary():
	print "This module reads the I/P document and prints \n \
		# Meaningful unique words \n \
		# Count of occurance in the document and \n \
		# Number of senses  "
	print "Usage : \n \
		$ " + sys.argv[0] +" input_file sort_mode \n\n \
		    input_file : Input text file which has to be analyzed\n \
		    sort_mode  : 1 : Sort Lexicographically \n \
		               : 2 : Sort by number of occurances \n \
			       : 3 : sort by number of senses \n \
		"

"""
Current stop words :
~~~~~~~~~~~~~~~~~~~~
a about above after again against ago all am an and any are as at be because 
been before being below between both but by call can come could day did do 
does doing don down during each few find first for from further get go had
has have having he her here hers herself him himself his how i if in into is
it its itself just like long look made make many may me more most my myself
no nor not now number of off oil on once one only or other our ours ourselves
out over own part people s said same see she should so some such t than that
the their theirs them themselves then there these they this those through time
to too two under until up use very was water way we were what when where which
while who whom why will with word would write you your yours yourself
yourselves
"""

def add_word(word):
	print word

# Main Function	
if __name__ == "__main__":

	# Input arguments check
	if(len(sys.argv) != 3):
		print_summary()
		sys.exit()

	# Variables declaration
	wordList = dict()
	concordList = []
	sort_mode = int(sys.argv[2])

	# Read stop words
	f_sw = open('stopwords.txt','r')
	stopwords = f_sw.read()

	# Print summary of the module
	#print_summary()

	# Read the document into string
	f = open(sys.argv[1],'r')
	text = f.read()
	print text

	# Split individual words in sentences
	for word in text.split():

		#remove punctuation, numbers, and newlines		
		word = word.translate(None,"0123456789,<>./?;:'\"{[]}\\=+_()*&^%$#@!~`’—")

		# Convert all strings into lowercase
		word = word.lower()
		
		# Add the word to the list
		if wordList.has_key(word):
			wordList[word] = wordList[word] + 1
		else:
			wordList[word] = 1

	# Check if the word is valid one with meaning available in wordnet DB and its not a stop word
	for rword in wordList: 
		wlen = len(wn.synsets(rword))
		if rword not in stopwords and wlen is not 0:
			entity=(rword,wordList[rword],wlen)
			concordList.append(entity)

	# Sort Lexicographically
	if (sort_mode == 1):
		sorted_list = sorted(concordList,key=lambda concordList:concordList[0])
		i = 0
		for item in sorted_list:
			print "%20s %2d %2d" % (sorted_list[i][0], sorted_list[i][1], sorted_list[i][2])
			i=i+1

	# Sort by frequency within the document
	if (sort_mode == 2):
		sorted_list = sorted(concordList,key=lambda concordList:concordList[1])
		i = 0
		for item in sorted_list:
			print "%20s %2d %2d" % (sorted_list[i][0], sorted_list[i][1], sorted_list[i][2])
			i=i+1
	
	# Sort by senses in wordnet DB
	if (sort_mode == 3):
		sorted_list = sorted(concordList,key=lambda concordList:concordList[2])
		i = 0
		for item in sorted_list:
			print "%20s %2d %2d" % (sorted_list[i][0], sorted_list[i][1], sorted_list[i][2])
			i=i+1


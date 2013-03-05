#!/usr/bin/env python
#! -*- coding: utf-8 -*-
#
# CheaterPress (LetterPress Cheat) is dedicated to the new word game LetterPress.
# Enter all 25 letters from the 5 by 5 game board and you'll get a list of all the words that you can spell.
# 
# Boubakr NOUR <n.boubakr@gmail.com>


import sys


def loadWords(dictionary_file):
	"""
	Loads words from the dictionary file, and returns a list of valid words.
	"""
	wordList = list()
	
	# Depending on the size of the word list, this function may take some time
	print "[!] Loading word list from the dictionary file..."
	with open(dictionary_file) as dictionary:
		wordList = [word.strip().lower() for word in dictionary.readlines()]
	print "[!] %d words loaded..." % len(wordList)

	return wordList


def findWords(letters):
	"""
	Returns a list with all words that can be constructed from the given letters.
    """
	letters = letters.replace(' ', '')
	letters = list(letters.strip().lower())

	wordList = loadWords("/usr/share/dict/words")
	# List to store found words
	foundWords = list()

	print "[!] Finding words..."
	for word in wordList:
		word_as_list = list(word)
		for letter in letters:
			if letter in word_as_list:
				word_as_list.remove(letter)

		if len(word_as_list) == 0:
			foundWords.append(word)

	return foundWords


if __name__ == '__main__':

	print "Welcome to CheaterPress\n"

	if len(sys.argv) < 2 or len(sys.argv[1]) < 6:
		print "ERROR: Enter all 25 letters !"
		sys.exit(1)

	letters = sys.argv[1]
	if len(sys.argv) > 2:
		for i in range(2, len(sys.argv)):
			letters = letters + sys.argv[i]

	# Get solution :)
	solution = findWords(letters)
	solution.sort(key=len)

	if len(solution) == 0:
		print "[!] No words founds !"
		sys.exit(0)
	else:
		print "[!] %d words found !" % len(solution)

	raw_input("Get Words ?!")

	min_lenghth = len(solution[0])
	max_length = len(solution[-1])

	tmp = list()
	for length in range(min_lenghth, max_length + 1):
		print "\n%d Letters LetterPress Words:" % length
		print "-----------------------------"

		for word in solution:
			if len(word) == length:
				tmp.append(word)
				solution.remove(word)
		print ", ".join(map(str, tmp))
		del tmp[:]
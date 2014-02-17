#!/usr/bin/env python
# Author: s905060

import sys
import hashlib
import string

# Generating Rainbow table hashed_and_plain from Yahoo password
# Please download the wordlist from crackstation.net 
def MD5():
	for line in open("crackstation-human-only.txt"):
			md5 = line
			hashed = hashlib.md5(md5).hexdigest()
			plaintext = line
			result = hashed + " " + plaintext
			print "Writing process: " + result
			f = open("stored_and_plaintxet_MD5.txt", 'a')
			f.write(result)
			f.close
	
	eharmony_passwords_list = []
	for test in open("eharmony_passwords.txt"):
		eharmony_passwords_list.append(test)
	iteration = 0

# Search the MD5 hashed password
	for line in open("stored_and_plaintxet_MD5.txt"):
		iteration += 1
		if iteration %1000 == 0:
			sys.stdout.write(".")
			sys.stdout.flush()
		columns = line.split(' ')
		if len(columns) >= 2:
			md5 = columns[0]
			plaintext = columns[1]
			#print "MD5 matching: " + md5
			#for test in open("eharmony_passwords.txt"):
			if md5 in eharmony_passwords_list:
				result = (md5 + " " + plaintext + " From:eharmony_passwords.txt")
				print "MD5 cracked: " + result
				f = open("MD5_cracked.txt", 'a')
				f.write(result)
				f.close

def SHA256_salt():
	for line in open("crackstation-human-only.txt"):
		SHA = line
		for salt in xrange(0,100):
			salt = "%02d" % salt
			Salted_SHA = salt+SHA		
			hashed = hashlib.sha256(Salted_SHA).hexdigest()
			plaintext = Salted_SHA
			result = hashed + " " + plaintext
			print "Writing process: " + result
			f = open("stored_and_plaintxet_SHA256_salt.txt", 'a')
			f.write(result)
			f.close

	formspring_list = []
	for test in open("formspring.txt"):
		formspring_list.append(test)
	iteration = 0
	
# Search the MD5 hashed password
	for line in open("stored_and_plaintxet_SHA256_salt.txt"):
		iteration += 1
		if iteration %1000 == 0:
			sys.stdout.write(".")
			sys.stdout.flush()
		columns = line.split(' ')
		if len(columns) >= 2:
			SHA = columns[0]
			plaintext = columns[1]
			#print "SHA256 matching: " + SHA
			#for test in open("formspring.txt"):
			if SHA in formspring_list:
				result = (SHA + " " + plaintext + " From:formspring.txt")
				print "SHA256 cracked: " + result
				f = open("Sha256_saled_cracked.txt", 'a')
				f.write(result)
				f.close

print SHA256_salt()
print MD5()
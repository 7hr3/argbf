#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse, os, subprocess
from subprocess import Popen, PIPE

#Here we begin parsing our arguments.
parser = argparse.ArgumentParser(description='Brute force passwords as arguments.')
parser.add_argument('prog', metavar='prog', type=str, nargs='+', help='A program to bruteforce.')
parser.add_argument('--wordlist=', type=str, help="Provide a wordlist.", dest="wordlist", action="store", default=False)
parser.add_argument('--inc=', type=str, help="Provide the answer for an incorrect password.", dest="inc", action="store", default=False)

#Here we initialize the arguments.
args = parser.parse_args()

#Here we do checks to ensure every argument is provided.
if not args.inc:
     print "Incorrect phrase required."
     exit(0)

if not args.wordlist:
     print "Wordlist required."
     exit(0)

#This is our list that we will add words to.
words = []

#This opens the file as read-only for parsing each line.
with open(args.wordlist, "r") as myfile:
#This loop parses each line in the file.
     for line in myfile:
#Here we remove newline characters from each word.
          line = line.replace('\n','').replace('\r','')
#And finally we append the word to our list.
          words.append(line)

#Here is where the brute force occurs.
for word in words:
#Run the word against the program and store the result in answer var.
     answer = subprocess.Popen("./%s %s" % (args.prog[0],word), shell=True, stdout=PIPE, stderr=PIPE)
#Communicate with the pip and store the error and output of the command.
     answertext, answererror = answer.communicate()
#Cleanup the output to remove newlines.
     answertext = answertext.replace('\n','').replace('\r','')
#If the output does not match the incorrect passphrase output then we print the correct passphrase.
     if answertext != args.inc:
          print answertext
          print "Password is: %s" % word

#!/usr/bin/python

#FILENAME   : naive_bayes_tictactoe.py 
#PROGRAMMER : Vijay Koju
#CLASS      : CSCI 6350/7350 (Data Mining)
#DUE DATE   : 2/19/2013
#INSTRUCTOR : Dr. Li

import sys
from random import choice

# count the attributes
# input parameters :
# attr_list   -> list to count from
# val_str     -> count for val_str
# output :
# -> cnt -> count of val_str 
def count(attr_list,val_str):
	cnt = 0
	for i in range(len(attr_list)):
		if attr_list[i]==val_str:
			cnt += 1
	return cnt
		
# compute all the conditional probabilities of attribute values
# input parameters :
# train_file   -> training data file
# output :
# -> probabilities -> all the conditional probabilities
def compute_probabilities(train_file):
	file_handle = open(train_file, 'r') # open file
	a_line = file_handle.readline()     # readin the first line
	num_cols = len(a_line.split(","))   # count # of columns in file_handle
	file_handle.close()                 # close file

	file_handle = open(train_file, 'r') # open file again
	attr_val = ['x','o','b']            
	# initialize 2-d lists to store attributes
	class_positive = [[] for i in range(num_cols-1)]
	class_negative = [[] for i in range(num_cols-1)]
	
	for line in file_handle: # go through all the lines
		line = line.split(',')
		if line[-1] == "positive\n": # for class -> positive
			for i in range(num_cols-1):
				if line[i] == '?': # handle missing attribute value
					class_positive[i].append(choice(attr_val))
				else:              # store attribute values
					class_positive[i].append(line[i])
		else:                        # for class -> negative
			for i in range(num_cols-1):
				if line[i] == '?': # handle missing attribute value
					class_negative[i].append(choice(attr_val))
				else:              # store attriute values
					class_negative[i].append(line[i])
	
	num_positives = len(class_positive[0]) # # of positives
	#print num_positives
	num_negatives = len(class_negative[0]) # # of negatives
	#print num_negatives
	total_instances = num_positives + num_negatives # # total numbers
	#print total_instances
	
	# counts of each attribute value
	counts_positive = []
	counts_negative = []
	for i in range(3): # for class -> positive
		counts_positive.append(count(class_positive[3*i],'x'))
		counts_positive.append(count(class_positive[3*i],'o'))
		counts_positive.append(count(class_positive[3*i],'b'))
		counts_positive.append(count(class_positive[3*i+1],'x'))
		counts_positive.append(count(class_positive[3*i+1],'o'))
		counts_positive.append(count(class_positive[3*i+1],'b'))
		counts_positive.append(count(class_positive[3*i+2],'x'))
		counts_positive.append(count(class_positive[3*i+2],'o'))
		counts_positive.append(count(class_positive[3*i+2],'b'))
	for i in range(3): # for class -> negative
		counts_negative.append(count(class_negative[3*i],'x'))
		counts_negative.append(count(class_negative[3*i],'o'))
		counts_negative.append(count(class_negative[3*i],'b'))
		counts_negative.append(count(class_negative[3*i+1],'x'))
		counts_negative.append(count(class_negative[3*i+1],'o'))
		counts_negative.append(count(class_negative[3*i+1],'b'))
		counts_negative.append(count(class_negative[3*i+2],'x'))
		counts_negative.append(count(class_negative[3*i+2],'o'))
		counts_negative.append(count(class_negative[3*i+2],'b'))
	#print count(class_positive[0],'x')
	#print count(top_left_p,'x')
	#print counts_positive
	#print counts_negative
	
	probabilities  = []
	# probability of positives
	prob_positives = float(num_positives)/total_instances
	# probability of negatives 
	prob_negatives = float(num_negatives)/total_instances
	
	# conditional probabilities for positive class
	for i in range(len(counts_positive)):
		probabilities.append(float(counts_positive[i])/num_positives)
	
	# conditional probabilities for negative class
	for i in range(len(counts_negative)):
		probabilities.append(float(counts_negative[i])/num_negatives)
	
	probabilities.append(prob_positives)
	probabilities.append(prob_negatives)
	
	#print probabilities[-3]
	#print len(probabilities)
	#print probabilities
	file_handle.close()
	return probabilities # return probabilities

# predict class based on the probabilities from training data
# input parameters :
# p            -> list of conditional probabilities from training data
# a1,a2,...,a9 -> attribute values
# output :
# -> class -> positive or negative
def classify(p,a1,a2,a3,a4,a5,a6,a7,a8,a9):
	attrs = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
	for i in range(len(attrs)):
		if attrs[i] == '?': # handle missing attribute value
			attrs[i] = choice(['x','o','b']) # assign random attribute value
	#print attrs
	p_pos = []
	p_neg = []
	# calculate naive bayes density estimator
	for i in range(len(attrs)):
		if attrs[i]=='x':
			p_pos.append(p[3*i])
			p_neg.append(p[3*i+27])
		elif attrs[i]=='o':	
			p_pos.append(p[3*i+1])
			p_neg.append(p[3*i+28])
		elif attrs[i]=='b':	
			p_pos.append(p[3*i+2])
			p_neg.append(p[3*i+29])
	net_p_pos = 1
	net_p_neg = 1
	# product of conditional probabilities
	for i in range(len(p_pos)):
		net_p_pos *= p_pos[i] # for positive
		net_p_neg *= p_neg[i] # for negative
	net_p_pos *= p[54] # multiply it with probability of positives
	net_p_neg *= p[55] # multiply it with probability of negatives
	#print net_p_pos, net_p_neg
	if net_p_pos > net_p_neg: # check which probability is higher
		return 'positive' # class -> postive
	else:
		return 'negative' # class -> negative

# predict classes for attribute values from a file
# input parameters :
# training_file   -> training data
# test_file       -> data file to classify
# output :
# -> predict the classes
# -> stats -> list of statistics
def test_class(training_file,test_file):
	test_handle = open(test_file,'r')
	p=compute_probabilities(training_file) # compute conditional probs 
	rights = 0
	wrongs = 0
	for line in test_handle: # for attributes in file
		line = line.split(',')
		cc = classify(p,line[0],line[1],line[2],line[3],line[4],line[5],line[6],line[7],line[8]) # predict class
		if cc == line[9].strip('\n'):
			rights += 1 # count # of right predictions
		else:
			wrongs += 1 # count # of wrong predictions
	test_handle.close()
	total = rights+wrongs # total counts
	error = (float(wrongs)/total)*100 # compute error percentage
	stat = [total, rights, wrongs, error] # list of statistics
	print "        tested %d,         errors %d(%.2f%%)"%(total,wrongs,error)
	return stat

# print probabilities on standard output
# input parameters :
# p      -> list of conditional probabilities
# output:
# print probabilities
def print_probabilities(p):
	print "---------------------------------------------------------------"
	print "Probabilities from the training data set."
	print "positive : "+str("%.5G"%p[54])
	print "negative : "+str("%.5G"%p[55])
	print "-------------------------- positive ---------------------------"
	print "top-left square     : x => "+str("%.5G"%p[0])+" o => "+str("%.5G"%p[1])+" b => "+str("%.5G"%p[2])
	print "top-middle square   : x => "+str("%.5G"%p[3])+" o => "+str("%.5G"%p[4])+" b => "+str("%.5G"%p[5])
	print "top-right square    : x => "+str("%.5G"%p[6])+" o => "+str("%.5G"%p[7])+" b => "+str("%.5G"%p[8])
	print "middle-left square  : x => "+str("%.5G"%p[9])+" o => "+str("%.5G"%p[10])+" b => "+str("%.5G"%p[11])
	print "middle-middle square: x => "+str("%.5G"%p[12])+" o => "+str("%.5G"%p[13])+" b => "+str("%.5G"%p[14])
	print "middle-right square : x => "+str("%.5G"%p[15])+" o => "+str("%.5G"%p[16])+" b => "+str("%.5G"%p[17])
	print "bottom-left square  : x => "+str("%.5G"%p[18])+" o => "+str("%.5G"%p[19])+" b => "+str("%.5G"%p[20])
	print "bottom-middle square: x => "+str("%.5G"%p[21])+" o => "+str("%.5G"%p[22])+" b => "+str("%.5G"%p[23])
	print "bottom-right square : x => "+str("%.5G"%p[24])+" o => "+str("%.5G"%p[25])+" b => "+str("%.5G"%p[26])
	print "-------------------------- negative ---------------------------"
	print "top-left square     : x => "+str("%.5G"%p[27])+" o => "+str("%.5G"%p[28])+" b => "+str("%.5G"%p[29])
	print "top-middle square   : x => "+str("%.5G"%p[30])+" o => "+str("%.5G"%p[31])+" b => "+str("%.5G"%p[32])
	print "top-right square    : x => "+str("%.5G"%p[33])+" o => "+str("%.5G"%p[34])+" b => "+str("%.5G"%p[35])
	print "middle-left square  : x => "+str("%.5G"%p[36])+" o => "+str("%.5G"%p[37])+" b => "+str("%.5G"%p[38])
	print "middle-middle square: x => "+str("%.5G"%p[39])+" o => "+str("%.5G"%p[40])+" b => "+str("%.5G"%p[41])
	print "middle-right square : x => "+str("%.5G"%p[42])+" o => "+str("%.5G"%p[43])+" b => "+str("%.5G"%p[44])
	print "bottom-left square  : x => "+str("%.5G"%p[45])+" o => "+str("%.5G"%p[46])+" b => "+str("%.5G"%p[47])
	print "bottom-middle square: x => "+str("%.5G"%p[48])+" o => "+str("%.5G"%p[49])+" b => "+str("%.5G"%p[50])
	print "bottom-right square : x => "+str("%.5G"%p[51])+" o => "+str("%.5G"%p[52])+" b => "+str("%.5G"%p[53])
	print "---------------------------------------------------------------"

# print help
def print_help():
	print "--------------- Command line options ----------------"
	print " ./naive_bayes_tictactoe.py"
	print "===>>> print this page "
	print " "
	print " ./naive_bayes_tictactoe.py train_file"
	print "===>>> print probability table"
	print " "
	print " ./naive_bayes_tictactoe.py train_file test_file"
	print "===>>> classify the items in filename according to their attributes"
	print " "
	print " ./naive_bayes_tictactoe.py train_file a1 a2 a3 a4 a5 a6 a7 a8 a9"
	print "===>>> predict class of a1 a2 a3 a4 a5 a6 a7 a8 a9"
	print " "

# main function
if __name__ == '__main__':
	# if # of command-line argument is 1
	if len(sys.argv) == 1:
		print_help() # print help
	# if # of command-line argument is 2
	elif len(sys.argv) == 2:
		train_file = str(sys.argv[1]) # training file
		p=compute_probabilities(train_file) # compute conditional probs
		print_probabilities(p) # print probabilities
	# if # of command-line argument is 3
	elif len(sys.argv) == 3:
		train_file = str(sys.argv[1]) # training file
		test_file = str(sys.argv[2])  # test file
		test_class(train_file,test_file) # predict class
	# if # of command-line argument is 1
	if len(sys.argv) == 11:  
		train_file = str(sys.argv[1]) # training file
		p = compute_probabilities(train_file) # compute conditional probs
		cc = classify(p,sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10]) # predict class
		print cc # print class

#!/usr/bin/python

#FILENAME   : cross_validation.py 
#PROGRAMMER : Vijay Koju

import generate_data as gd
import naive_bayes_tictactoe as nb

# do cross-validation test
# input parameters :
# file_name   -> input data file
# n_folds     -> # of folds for cross-validation
# output:
# -> do cross-validation test and print average error percentage
def cross_validate(file_name,n_folds):
	file_handle = open(file_name,'r') # open file
	num_lines = gd.getNumLines(file_handle) # # of lines in file
	# generate 10 data sets for 10-fold cross-validation
	files = gd.genDataN(file_name,num_lines,10,n_folds)
	stats = []
	print "------------------------------------------------"
	print '10-fold cross validation for '+file_name
	print "------------------------------------------------"
	for i in range(n_folds):
		test_file = files[i] # test file name
		rest_of_files = []
		for j in range(n_folds):
			if j != i:
				rest_of_files.append(files[j]) # list of names of rest of the files
		#print rest_of_files
		train_file = 'cross_validate_train.data' # new training data file name
		gd.mergeFiles(rest_of_files,train_file) # merge data -> training data
		st = nb.test_class(train_file,test_file) # predict class
		stats.append(st)   # saves statistics
		gd.deleteFile(train_file) # delete merged training data
	#print stats
	avg_total = 0  # average # of tests
	avg_rights = 0 # average # of rights
	avg_wrongs = 0 # average # of wrongs
	avg_error = 0  # average error percentage 
	for i in range(len(stats)):
		avg_total += stats[i][0]
		avg_rights += stats[i][1]
		avg_wrongs += stats[i][2]
		avg_error += stats[i][3]
	avg_total /= float(len(stats))
	avg_rights /= float(len(stats))
	avg_wrongs /= float(len(stats))
	avg_error /= float(len(stats))
	print "------------------------------------------------"
	print "Average tested %.2f, Average errors %.2f(%.2f%%)"%(avg_total,avg_wrongs,avg_error)
	print "------------------------------------------------"
	
# main function
if __name__ == '__main__':
	for i in range(1,11): # 10-fold cross validation for 10 diff data sets
		file_name = 'tic-tac-toe'+str(10*i)+'.data'
		cross_validate(file_name,10) # 10-fold cross validation

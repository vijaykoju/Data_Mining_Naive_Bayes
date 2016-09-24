#!/usr/bin/python

#FILENAME   : generate_data.py 
#PROGRAMMER : Vijay Koju
#CLASS      : CSCI 6350/7350 (Data Mining)
#DUE DATE   : 2/19/2013
#INSTRUCTOR : Dr. Li

import random
import math
import linecache
import sys
import os

# get number of lines of a file
# input parameter :
# file_handle   -> input file handler
# output :
# -> lines -> # of lines in input file
def getNumLines(file_handle):
	lines = 0
	buf_size = 1024*1024
	read_f = file_handle.read
	buf = read_f(buf_size)
	while buf:
		lines += buf.count('\n')
		buf = read_f(buf_size)
	return lines

# get certain percent of data from a file randomly and save it in a
# different file
# input parameters :
# file_name    -> input file
# num_lines    -> # of lines in file_name
# percentage   -> % of data to be extracted and saved in a new file
# output :
# -> data file created in the current folder
def genData(file_name,num_lines,percentage):
	num_data = math.floor((percentage/100.0)*num_lines)
	rand_list = random.sample(range(num_lines),int(num_data))
	with open(file_name.split('.')[0]+str(percentage)+'.data','w') as f1:
		for i in range(len(rand_list)):
			f1.write(linecache.getline(file_name,rand_list[i]))
	
# generate n data files for N-fold cross-validation
# input parameters :
# file_name    -> input file
# num_lines    -> # of lines in file_name
# percentage   -> % of data to be extracted and saved in a new file
# n            -> # of data files to be generated
# output :
# -> n data files created in the current folder
# -> f_list -> list of newly generated data file names
def genDataN(file_name,num_lines,percentage,n):
	num_data = math.floor((percentage/100.0)*num_lines)
	f_list = []
	for i in range(n):
		rand_list = random.sample(range(num_lines),int(num_data))
		f_list.append(file_name.split('.')[0]+'.ro'+str(i))
		with open(file_name.split('.')[0]+'.ro'+str(i),'w') as f1:
			for j in range(len(rand_list)):
				f1.write(linecache.getline(file_name,rand_list[j]))
	return f_list

# merge several data files into one
# input parameters :
# f_list           -> list of file names to be merged into one
# merged_file_name -> name of file to be merged into
# output :
# -> merged data file
def mergeFiles(f_list,merged_file_name):
	with open(merged_file_name,'w') as f1:
		for f in f_list:
			with open(f,'r') as f2:
				f1.write(f2.read())
					
# delete a data file
# input parameters :
# file_name   -> file name to be deleted
# output :
# file_name deleted if it exits
def deleteFile(file_name):
	if os.path.isfile(file_name):
		os.remove(file_name)
	else:
		print "Error:%s file not found"%file_name

def main():
	if (len(sys.argv) != 2):
		print "Not enough arguments."
		print "Usage:"
		print "      ./generate_data.py [filename]"
		exit()
	file_name = str(sys.argv[1])
	file_handle = open(file_name,'r')
	num_lines = getNumLines(file_handle)
	for i in range(1,11): # create 10 data files with 10, 20, ... ,100 % data
		genData(file_name,num_lines,10*i)
	#a = genDataN(file_name,num_lines,10,10)
	#print a
	#mergeFiles(a,'merged.data')
	#deleteFile('merged.data')
	file_handle.close()

if __name__ == '__main__':
	main()

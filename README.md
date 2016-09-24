PROGRAMMER : Vijay Koju

Data files used : 

1) tic-tac-toe.data

2) tic-tac-toe.names

3) test.data

Python programs : 

1) generate_data.py

2) naive_bayes_tictactoe.py

3) test.py
								
4) cross_validation.py

generate_data.py :

Take in tic-tac-toe.data as input file through command-line argument and produces 10 data sets with 10%, 20%, ..., 90%, and 100% of randomly selected data from tic-tac-tae.data.

The output files are named as:

tic-tac-toe10.data

tic-tac-toe20.data

...

tic-tac-toe100.data

naive_bayes_tictactoe.py :

Perform Naive Bayes analysis and predict class for new data.

test.py :

This program is just for testing purpose to see if the probabilities calculated by naive_bayes_tictactoe.py are correct. It uses test.data file for testing. I compared the probabilities computed by hand and by naive_bayes_tictactoe.py to confirm the results. They match.

cross_validation.py :

Perform 10-fold cross-validation on each of the 10 data files outputed by generate_data.py. For each cross-validation is creates 10 additional data files with 10% data (randomly chosen) of its parent file. It prints out the statistics of 10-fold cross-validations.

Usage:

To generate data files

	$ ./generate_data.py tic-tac-toe.data

To perform naive bayes analysis

	$ ./naive_bayes_tictactoe.py
      or
	$ ./naive_bayes_tictactoe.py training_data_file
      or
	$ ./naive_bayes_tictactoe.py training_data_file test_data_file
      or
	$ ./naive_bayes_tictactoe.py training_data_file a1 a2 a3 a4 a5 a6 a7 a8 a9

To perform 10-fold cross-validation

	$ ./cross_validation.py

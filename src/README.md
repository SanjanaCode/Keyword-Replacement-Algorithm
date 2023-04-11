# Source Code

This folder contains the source code for algorithm 1 and 2 for the keyword replacement algorithm.

## Algorithm 1

`naiveApproachAlgorithm.py` contains the source code for the naive approach algorithm (Algorithm 1). The algorithm uses brute force technique where it takes in each tweet and a list of common abbreviations and keywords. The algorithm then replaces the common abbreviations and keywords with their full form. The algorithm then returns the tweet list with the common abbreviations replaced with their full form.

## Algorithm 2

`optimizedApproachAlgorithm.py` contains the source code for the optimized approach algorithm (Algorithm 2). The algorithm uses a avl tree data structure to store the common abbreviations and keywords. The algorithm then takes in each tweet and seraches for the abbreviations in the AVL tree and replaces them with their full form, if it finds any matches. The algorithm then returns the tweet list with the abbreviations replaced with their full form.

## Helper Functions

`helperFunctions.py` contains the source code for the helper functions to calculate the time taken to run different input sizes for the algorithms. This function is then used to plot the time taken for the algorithms to run for different input sizes.

## Python notebooks

`Naive-Approach.ipynb` contains the python notebook for the naive approach algorithm (Algorithm 1). The notebook contains the code for the reading the excel files and converting tweets into lists and abbreviations into dictionaries. It runs the algorithm and also plots the time taken for the algorithm to run for different input sizes.

`Optimized-Approach.ipynb` contains the python notebook for the naive approach algorithm (Algorithm 2). The notebook contains the code for the reading the excel files and converting tweets into lists and abbreviations into dictionaries. It runs the algorithm and also plots the time taken for the algorithm to run for different input sizes.

# MashineLearningFromScratch
Own linear regression alghoritm from scratch!

resources:
  http://mezeylab.cb.bscb.cornell.edu/labmembers/documents/supplement%205%20-%20multiple%20regression.pdf
  https://medium.com/@lope.ai/multivariate-linear-regression-from-scratch-in-python-5c4f219be6a
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3049417/

data from: https://archive.ics.uci.edu/ml/datasets/Student+Performance

Goals of this project:

  Mastering implementation of algorithms 
  
  Trying to make alghoritm using only non-video explanations
  
  Getting better understanding of linear regression
  
  Learning how to use cython

How to install:

1. dowloand files

2. install cython (pip install cython or pip3 install cython)

// (install other packages that you dont have)

3. Try to run 'exaple.py', if its showing you iterations thats mean you are ready to go!
  
4. if it gives you errors, try:

  - 'python3 setup.py build_ext --inplace' in folder where you have  
    setup.py
    
  - Check if you have weights.cfg if you are trying to load model
    (LOAD_MODEL is True in exaple.py)
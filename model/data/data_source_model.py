"""
Data Source controller module.
"""

import sys
import pandas as pd
import csv
sys.dont_write_bytecode = True
import controller.Upload


# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("data/bd-dec17-births-deaths-by-region.csv") 

# Preview the first 5 lines of the loaded data 
data.head()



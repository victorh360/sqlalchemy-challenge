# sqlalchemy-challenge

## Overview

For the Module 10 Challenge we were tasked with performing a climate analysis on Honolulu Hawaii. We were to create a notebook and an app, starter files were provided for both along with the data we were to analize.

## Contents

- Resources- This directory contains the sqlite and csv files that were analized.
- analysis.ipynb- This notebook contains the analysis of the data. 
- app.py- This file contains the code for the app.

## Resources

For most of this assignment I was able to reference examples that we completed during class.

- I used code from excercise 10.3 to find the most recent date in the data set for my analysis.

'''
session.query(Measurement.date).order_by(Measurement.date.desc()).first()
'''

- I used https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hist.html to derive the correct syntax for the histogram.


## Notes

- The precipitation graph in the starter code solution does not match the graph in the assignment instructions. I struggled trying to get my graph to match, a classmate pointed out this discrepancy to me.

- I was able to pull most of the query code for the app from the analysis workbook.

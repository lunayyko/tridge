# Tridge coding assignment

## Instruction
* Install Python3: follow instructions in <https://realpython.com/installing-python>
* From the command line: 
  * `git clone https://github.com/lunayyko/tridge.git`
  * `cd tridge`
* Question 1: `python calender.py`
  * Project Euler #19: How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)? 
* Question 2: `python baseconverter.py`
  * Running this file will print result of test cases.
* Question 3:
  * How would you normalize (parsing, pre-processing, grouping) this data to simplify it’s processing into a database ?
   - I'd group based on quality(First Quality, ) per same variety.
  * What additional value can you extract from this dataset ? If you find any please explain how would you collect it (pseudo-algorithm)
   - Linear Regression graph with time as x-coordinate would make it easy to check range of price for same quality group throughout season and to spot irregular price surge or drop.
  * How would you approach the script of putting this information into a database ?(Concurrency, Scale, Prerequisites, etc..)
   - By writing db_uploader python file to import csv file into database.    

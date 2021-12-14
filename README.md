# Tridge coding assignment


## Instruction


Install Python3: follow instructions in <https://realpython.com/installing-python>
* From the command line: 
  * `git clone https://github.com/lunayyko/tridge.git`
  * `cd tridge`

## Assignment


1. Calendar Problem

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31
Dec 2000)?

2. Base Converter

Language Requirement: Python. 
Implement the `_convert` method of the following class:

```python
class Transformer(object):
Convert numbers from base 10 integers to base N strings and back again.
Sample usage:
>>> base20 = Transformer('0123456789abcdefghij')
>>> base20.from_decimal(1234)
'31e'
>>> base20.to_decimal('31e')
1234
decimal_digits = '0123456789'
def __init__(self, digits):
self.digits = digits
def from_decimal(self, i):
return self._convert(i, self.decimal_digits, self.digits)
def to_decimal(self, s):
return int(self._convert(s, self.digits, self.decimal_digits))
def _convert(self, number, fromdigits, todigits):
raise NotImplementedError
binary_transformer = Transformer('01')
hex_transformer = Transformer('0123456789ABCDEF')
base62_transformer =
Transformer('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz')
```

3. Dataset

Language Requirement: None

This question is an open-question to gauge your ability to understand a dataset and your
approach to extract value from it.

No code is required and there is no single-right answer, you are free to elaborate on any
infrastructure or data-structure that you deem valid for this use case.

You are given the attached dataset of price information for products. You are then asked to
“normalize” and extract value out of this dataset.


How would you normalize (parsing, pre-processing, grouping) this data to simplify it’s processing into a database ?
What additional value can you extract from this dataset ? If you find any please explain how would you collect it (pseudo-algorithm)
How would you approach the script of putting this information into a database ?(Concurrency, Scale, Prerequisites, etc..)

This assignment will be due before October 31, 2021 . Please make sure to submit your work before then.


## Answer


1: run `python calender.py`
  * Project Euler #19: How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)? 
  * Running this file will print total days and sundays which is 171

2: run `python baseconverter.py`
  * Running this file will print result of test cases.

3: written under question
  * How would you normalize (parsing, pre-processing, grouping) this data to simplify it’s processing into a database ?
    * I'd group based on quality(First Quality) and variety.
    
  * What additional value can you extract from this dataset ? If you find any please explain how would you collect it (pseudo-algorithm)
    * Linear Regression graph with time as x-coordinate would make it easy to check range of price for same quality group throughout season and to spot irregular price surge or drop.
  
  * How would you approach the script of putting this information into a database ?(Concurrency, Scale, Prerequisites, etc..)
    * By writing db_uploader python file to import csv file into database.    


##How to reproduce results.


#1. Install Radon via terminal

```
pip install radon
```
#2. Use radon to analyse core directory

Stand in pandas root directory!
```
radon cc pandas/core -a
```
Outputs large list of ratings.
...
Average complexity: A (3.9910697320919626)

#3. Print ratings and complexity scores
```
radon cc pandas/core -s
```
Outputs large list of all ratings

#4. Create a JSON in your current directory
```
radon cc pandas/core -j > core_complexity.json
```
Creates json in directory you stand in.

#5. Further analyse using provided functions

1. Insert JSON in same folder as data parser.py and run data parser.py
-> You should get a CSV file with all files with complexity over 10.
2. Run Data Sorter.py
-> You should get top 10 complexity scores in the terminal, and a total amount of function with a complexity score over 10.
-> You should get another CSV file with the top 10 complexity scores.



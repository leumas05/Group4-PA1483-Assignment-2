import pandas as pd
import numpy as np
import timeit
import csv

# Dataset
print(f"Running test for Pandas version: {pd.__version__}")
df = pd.DataFrame(np.random.randn(1000000, 2), columns=['A', 'B'])

# Define opertaion
def run_groupby():
    df.groupby('A').sum()

# Measure time
execution_time = timeit.timeit(run_groupby, number=10) / 10
print(f"Avrage execution time: {execution_time:.4f} seconds")

# Save to CSV
with open('execution_results.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([pd.__version__, execution_time])
import pandas as pd
import numpy as np
import time
import os
import csv

file_name = 'testdata.csv'

# Test data 2 million lines.
if not os.path.exists(file_name):
    print("Generating testdata...")
    df_temp = pd.DataFrame(np.random.randn(2000000, 4), columns=['A', 'B', 'C', 'D'])
    df_temp.to_csv(file_name, index=False)

# File size in MB
file_size_mb = os.path.getsize(file_name) / (1024 * 1024)

# Measure read time
print("Läser in fil...")
start_time = time.time()
df = pd.read_csv(file_name)
end_time = time.time()

read_time = end_time - start_time
throughput = file_size_mb / read_time

print(f"Filesize: {file_size_mb:.2f} MB")
print(f"Read Time: {read_time:.4f} seconds")
print(f"Throughput: {throughput:.2f} MB/s")

# Spara resultatet till CSV
with open('io_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['File Size (MB)', 'Read Time (s)', 'Throughput (MB/s)'])
    writer.writerow([file_size_mb, read_time, throughput])
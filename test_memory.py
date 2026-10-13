import pandas as pd
import sys
import csv

# Create large dictionary with standard-Python
data_length = 1000000
raw_data = {
    'col1': [1] * data_length,
    'col2': ['test_string'] * data_length
}

# Measure raw data size
raw_size_bytes = sys.getsizeof(raw_data) + sum(sys.getsizeof(v) for v in raw_data.values())

# Convert to Pandas DataFrame and measure memory usage
df = pd.DataFrame(raw_data)
pandas_size_bytes = df.memory_usage(deep=True).sum()

# calculate overhead-ratio
ratio = pandas_size_bytes / raw_size_bytes

print(f"Size in standard-Python: {raw_size_bytes} bytes")
print(f"Size in Pandas: {pandas_size_bytes} bytes")
print(f"Memory Overhead Ratio: {ratio:.2f}")

# Save to csv
with open('memory_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Raw Size (bytes)', 'Pandas Size (bytes)', 'Ratio'])
    writer.writerow([raw_size_bytes, pandas_size_bytes, ratio])
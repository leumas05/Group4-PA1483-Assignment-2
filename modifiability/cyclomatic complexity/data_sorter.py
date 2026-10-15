#Code was generated using copilot.
#Prints top 10 complex files. And makes a CSV of it.
#Requires pandas.

import pandas as pd

df = pd.read_csv("complexity_over_10.csv")

top10 = df.sort_values(
    by="Complexity",
    ascending=False
).head(10)

print(top10)
print(f'Total values below B rating (<10): {len(df)}')

top10.to_csv("top10_complexity.csv", index=False)
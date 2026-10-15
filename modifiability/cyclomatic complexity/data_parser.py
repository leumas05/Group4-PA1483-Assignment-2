#Code was generated using copilot
#Creates a csv out of json that only has scores "C" or lower. C<10

import json
import csv

def export_complexity_over_10(json_file, csv_file):
    with open(json_file, "r") as f:
        data = json.load(f)

    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["File", "Function", "Complexity", "Rank"])

        for file_path, entries in data.items():
            for entry in entries:
                complexity = entry.get("complexity", 0)

                if complexity > 10:
                    writer.writerow([
                        file_path,
                        entry.get("name", ""),
                        complexity,
                        entry.get("rank", "")
                    ])

# Example usage
export_complexity_over_10(
    "core_complexity.json",
    "complexity_over_10.csv"
)
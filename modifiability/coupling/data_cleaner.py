#This code was generated using copilot to extract and clean information.
#This takes a json file and makes a CSV, where degree of coupling is stronger than 10%.
#Also removes connection to "No Component".

import json
import csv

with open("couplings_core.json") as f:
    data = json.load(f)

with open("coupling_core_results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "component_1",
        "component_2",
        "degree_of_coupling",
        "average_revisions"
    ])

    for row in data:
        degree = int(row["degree"])

        if degree >= 10 and row["entity"] != "No Component":
            writer.writerow([
                row["entity"],
                row["coupled"],
                degree,
                row["average-revs"]
            ])
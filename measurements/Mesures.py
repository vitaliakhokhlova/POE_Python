import csv

with open("Mesures.csv") as f:
    reader = csv.DictReader(f, delimiter=";")
    theoreticals = []
    measures = []
    for row in reader:
        theoretical = float(row["good"])
        measure = float(row["bad"])
        theoreticals.append(theoretical)
        measures.append(measure)

import numpy as np

t = np.array(theoreticals)
print(t)
m = np.array(measures)
print(m)
diff = m - t
print(diff)
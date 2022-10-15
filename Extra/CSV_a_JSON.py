import pandas as pd
import csv
import json
dato = pd.read_csv("Programación.csv")
print(dato)
print("Convertir a JSON: ")
print(json.dumps(list(csv.reader(open("Programación.csv")))))

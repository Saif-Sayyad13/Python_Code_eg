import kagglehub
import pandas as pd
import os

path = kagglehub.dataset_download("arshid/iris-flower-dataset")

df = pd.read_csv(os.path.join(path, "IRIS.csv"))

print(df.head(10))
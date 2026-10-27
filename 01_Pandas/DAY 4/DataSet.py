'''import pandas as pd

data = {
    'NAME': ['a', 'b', 'c', 'd'],
    'age': [23, 45, 66, 78],
    'sal': [1000, 2000, 3000, 4000],
    'dept': ['hr', 'anaylsis', 'it', 'hr'],
}
df = pd.DataFrame(data)
a=df.groupby('dept')['sal'].value_counts()
print(a)
b=df.groupby("dept")['sal'].mean()
print(b)
c=df.groupby("dept")['sal'].count()
print(c)
d=df.groupby("dept")['sal'].agg(['mean','sum','count'])
print(d)
e=df.query("age>45")
print(e)'''

'''
import kagglehub
import pandas as pd
import os

# 1. Download the dataset
path = kagglehub.dataset_download("arshid/iris-flower-dataset")

# 2. Load the dataset into a Pandas DataFrame
df = pd.read_csv(os.path.join(path, "IRIS.csv"))

# 3. Display the first 10 rows
print(df.head(10))
numb=df.select_dtypes(include="number")
print(numb)
print(df.describe())
print(df.describe(include="object"))
print(df.describe(include="All"))
print(df.describe(include="number"))

a=df['petal_length']
print(a)
b=df[df['petal_length']>4.5].head()
print(b)
c=df[df['species']=='Iris-virginica']
print(c)'''



'''C. species
• Average sepal_length
• Maximum petal_width
• Standard deviation of sepal_width
Create a new column:
D. "petal_ratio" = petal_length / petal_width
• For each species, find the average petal_ratio.
a=df.groupby("species").agg({"sepal_length":"max","petal_width":"max","sepal_width":"std"})
print(a)
b=df['sepal_length'].mean()
print(b)
c=df['petal_width'].max()
print(c)
c=df['sepal_width'].std()
print(c)
d=df["petal_ratio"] = df["petal_length"] / df["petal_width"]
print(d)
e= df.groupby("species")["petal_ratio"].mean()
print(e)'''

import pandas as pd
import os 
import kagglehub

path = kagglehub.dataset_download("yasserh/titanic-dataset")

print("Path to dataset files:", path)
df = pd.read_csv(os.path.join(path, "IRIS.csv"))

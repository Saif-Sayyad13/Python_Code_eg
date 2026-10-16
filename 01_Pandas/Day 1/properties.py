import pandas as pd
a=pd.Series([10,20,30,40,50,60,70,80,90,100])
print(a)
b=pd.Series([1,2,3,4,5])
print(b.nbytes)
c=pd.Series([10,15,20,21,26,27,70])
print(c.is_monotonic_increasing)
'''
import pandas as pd

name = ["A", None, "B", None]
age = [None, 23, None, 24]
sal = [7000, None, 8000, None]

# Fixed dictionary syntax: changed [] to {}
data = {"Name": name, "AGE": age, "SAL": sal} 
df = pd.DataFrame(data=data)

# 1) fillna() - Replace missing values with a specific value (e.g., 0 or "Missing")
df_fillna = df.fillna("Missing")

# 2) ffill() - Forward fill (carry forward the last valid observation)
df_ffill = df.ffill()

# 3) bfill() - Backward fill (pull backward the next valid observation)
df_bfill = df.bfill()

# 4) Rename columns - Fixed case-sensitivity typo from 'SAl' to 'SAL'
df_renamed = df.rename(columns={'SAL': 'S*L', 'Name': 'N1'})

df.drop('SAL',axis=1)
df.drop('SAL',axis=1,inplace=True) # this will detele permentely when we do inplace =True
'''

'''import pandas as pd
df=pd.DataFrame({'SUB':['PYTHON',"WEB",'JAVA'],"MockRAting":[1,2,3]})
df.loc[3]=["EXCEl",1.5]
df.loc[4]=["BI",3]
print(df)
df.loc[2,"MockRAting"]=[1] # is row no, '' col name 
print(df)
df['TOTAL']=0 # var_name['new-col_name']=default_Value
print(df)
aa=df.assign(c1=[11,12,13,14,15],c2=['a','b','c','d','e'])
print(aa)
df.insert(1,"Grade",["S","S1","Fail","A",'B'])
print(df)'''
'''
import pandas as pd

date_time = ["22-10-2026  16:21", "21-10-2026. 4:23", "17-09-2025 10:30"]
df = pd.DataFrame({'DATE_TIME': date_time})

df['DATE_TIME'] = pd.to_datetime(df["DATE_TIME"], format='mixed', dayfirst=True)

df['YEAR'] = df['DATE_TIME'].dt.year

print(df)
df['YEAR'] = df['DATE_TIME'].dt.year
df['MONTH'] = df['DATE_TIME'].dt.month
df['DAY'] = df['DATE_TIME'].dt.day
df['MONTH_NAME'] = df['DATE_TIME'].dt.month_name() 
df['DAY_NAME'] = df['DATE_TIME'].dt.day_name()
df['WEEK_DAY'] = df['DATE_TIME'].dt.weekday

print(df)'''

'''
import pandas as pd
name=["A","B","C","D"]
age=[1,2,3,4]
sal=[100,200,300,400]
data = {"Name": name, "AGE": age, "SAL": sal} 
df = pd.DataFrame(data=data)
print(df)
df["TOTAL"]=df["SAL"].agg([max,min,sum,])
print(df)
df'''

'''import pandas as pd
s=pd.Series([45,35,78,90,85,75])
print(s)
print(s.rank())
print(s.rank(ascending=False))'''

'''import pandas as pd
a=pd.Series([55,75,83,83,90,95])
y=pd.Series(a)
#print(a)
print(a.rank())
print(a.rank(ascending=False)) # rank method default present in mean avg
print(a.rank(method='min'))
print(a.rank(method='max'))
print(a.rank(method='average'))
print(a.rank(method='dense'))
print(a.rank(method='first'))'''

'''
import pandas as pd
name=['ravi','kiran','ram','naveen','krishna']
marks=[50,70,89,90,90]
data={'NAME':name,"MARKS":marks}
df=pd.DataFrame(data)
#print(df)
df["RANK"]=df["MARKS"].rank(method="average")
df["MAX"]=df["MARKS"].rank(method="max")
df["MIN"]=df["MARKS"].rank(method="min")
df["DENSE"]=df["MARKS"].rank(method="dense")
df["FIRST"]=df["MARKS"].rank(method="first")
print(df)'''



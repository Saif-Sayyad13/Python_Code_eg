import pandas as pd
name=['A','B','C','D','E','F']
age=[10,15,20,25,30,35]
sub=['Python','Java','SQL','Excel','PowerBI',"web-tech"]
sid=['a1','a2','a3','a4','a5','a6']
x={"NAME":name,"AGE":age,'SUB':sub,'SID':sid}
df=pd.DataFrame(x)
'''print(df)
print()
print(df.columns)
print()
print(df.shape)
print()
print(df.size)
print()
print(df.index)
print()
print(df.dtypes)
print()
print(df.axes)
print(df.values)
print()
print(df.ndim)
print()
print(df.empty)
print()
print(df.T)
print()
print(df.head())
print()
print(df.head(2))
print(df.tail())
print()
print(df.tail(1))
print()

print(df.info)
print()
print(df.sample())
print()
print(df.sample(2))
print()
print(df.info()) #when we use print function it will show none
df.info()
print()
print(df.describe())# by def num data type
print()
print(df.describe(include='number')) # same as num by default wala
print()
print(df.describe(include='object')) # to get or fetch char data
print()
print(df.describe(include='all')) # to fetch all data
print()
print(df["NAME"]) # to fetch single 
print()
print(df[['NAME','SID','SUB']]) # to fetch multiple col us nested 
print()'''
"""
1
df.loc[row_number]
 print(df.loc[2])
print()       
        

2. 
print(df.loc[3,["AGE"]])
print()

3. Row Range Selcetion



print(df.loc[0:4:1])# loc will include the end index
print()
print(df.iloc[0:4:1]) # i loc will work as slicing # i loc will excute the end index
print()

4.Row Range with Single Column

print(df.loc[0:2:1])
print()
print(df.loc[0:2:1,"SUB"])
print()

5.Row 
print(df.loc[0:2:1])
print()
print(df.loc[0:2:1,["NAME","SID"]])
print()


6.
print(df.loc[0:2:1])
print()
print(df.loc[0:2:1,"NAME":"SID"])
print()



print(df.loc[0:2:1,"NAME":"SID":2])
print()
print(df.loc[[0,4]])
print()
"""
'''
1.Single Row and Column
Syntax:-
df.iloc[row_number,[column_number]]

print(df.iloc[2,0])
print()
print(df.iloc[2,[0]])
print()
print(df.iloc[4,[3]])





2.Row Range and Column Range
Syntax:-
df.iloc[row_start:row_stop,col_start:col_stop]


print(df.iloc[0:3:1,0:2])




3.Row Range wit Single Column
Syntax:- 
df.iloc[start:stop,column_number]





4.Multiple Selected Row
Syntax:-
df.iloc[[row1,row2]]


print(df.iloc[0:4,2])

print(df.iloc[[]])'''
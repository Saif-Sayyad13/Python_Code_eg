'''
Merge
Syntax:-
NEW_var=pd.megre(left table righttable,ON=columns,how=Type of Joins)

'''
'''# creat a table
import pandas as pd

df1=pd.DataFrame({'ID':[1,2,3,4,5],"NAME":["A",'B','C','D','E']})
df2=pd.DataFrame({"ID":[2,3,4,6,7],"MARKS":[45,90,66,35,75]})
print(df1)
print(df2)
res=pd.merge(df1,df2,on="ID")# by default it take inner join
print(res)
res1=pd.merge(df1,df2,on="ID",how="inner")# her on me konsa table same hai wo anser aata 
print(res1)
res2=pd.merge(df1,df2,on="ID",how="outer")
print(res2)
res3=pd.merge(df1,df2,on="ID",how="left")
print(res3)
res4=pd.merge(df1,df2,on="ID",how="right")
print(res4)'''
'''
import pandas as pd

df1=pd.DataFrame({'ID':[1,2,3,4,5],"NAME":["A",'B','C','D','E']})
df2=pd.DataFrame({"RATING":[2,3,4,6,7],"MARKS":[45,90,66,35,75]})
res=pd.merge(df1,df2,left_on="ID",right_on="RATING")
print(res)
res1=pd.merge(df1,df2,left_on="ID",right_on="RATING",how="inner")
print(res1)
res2=pd.merge(df1,df2,left_on="ID",right_on="RATING",how="outer")
print(res2)
res3=pd.merge(df1,df2,left_on="ID",right_on="RATING",how="left")
print(res3)
res4=pd.merge(df1,df2,left_on="ID",right_on="RATING",how="right")
print(res4)'''
'''
import pandas as pd
df1=pd.DataFrame({'ID':[1,2,3,4,5],"NAME":["A",'B','C','D','E']})
df2=pd.DataFrame({"RATING":[2,3,4,6,7],"MARKS":[45,90,66,35,75]})
res=pd.concat([df1,df2])
print(res)
print(df1.join(df2))
res1=pd.concat([df1,df2],axis=0)
print(res1)
res2=pd.concat([df1,df2],axis=1)
print(res2)'''

import pandas as pd
import numpy as np
import random as r

num = np.arange(50,101)
df = pd.DataFrame(
    {
        'Name': ['PALAK','ABHAY','KARTIK','JANHAVI','HARSHIT','ARYAN','KANAV','ADITYA','AKHILESH','SURAJ']
    },
    index=(1,2,3,4,5,6,7,8,9,10)
)
df['Maths'] = list(r.choices(num, k=10))
df['Science'] = list(r.choices(num, k=10))
df['English'] = list(r.choices(num, k=10))
print()

print(df)
print()

maths_avg = np.mean(df.iloc[:,1])
science_avg = np.mean(df.iloc[:,2])
english_avg = np.mean(df.iloc[:,3])
print('Maths average: ',maths_avg)
print()
print('Science average: ',science_avg)
print()
print('English average: ',english_avg)
print()

highest = np.array(np.where((df['English']+df['Maths']+df['Science']) == max(df['English']+df['Maths']+df['Science'])))
print('Who got Highest marks: ',df.iloc[highest[0][0],0])
print()

df['Total'] = df['English'] + df['Maths'] + df['Science']
print(df)
print()

df['Result'] = np.where(df['Total'] > 150 , 'Pass', 'Fail')
print(df)
print()

df = df.sort_values('Total', ascending=False)
print(df)